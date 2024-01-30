import argparse
from functools import partial
from pathlib import Path
from typing import Optional

import numpy as np

try:
    import tomli
    from tqdm import tqdm
    from tqdm.contrib.concurrent import process_map
except ModuleNotFoundError as exc:
    msg = "Install 'tqdm' and 'tomli' to use the command line program."
    raise ModuleNotFoundError(msg) from exc

import pyvrp.search
from pyvrp import (
    GeneticAlgorithm,
    GeneticAlgorithmParams,
    PenaltyManager,
    PenaltyParams,
    Population,
    PopulationParams,
    ProblemData,
    RandomNumberGenerator,
    Result,
    Solution,
)
from pyvrp.crossover import selective_route_exchange as srex
from pyvrp.diversity import broken_pairs_distance as bpd
from pyvrp.read import INSTANCE_FORMATS, ROUND_FUNCS, read
from pyvrp.search import (
    NODE_OPERATORS,
    ROUTE_OPERATORS,
    LocalSearch,
    NeighbourhoodParams,
    compute_neighbours,
)
from pyvrp.stop import (
    MaxIterations,
    MaxRuntime,
    MultipleCriteria,
    NoImprovement,
)


def tabulate(headers: list[str], rows: np.ndarray) -> str:
    """
    Creates a simple table from the given header and row data.
    """
    # These lengths are used to space each column properly.
    lens = [len(header) for header in headers]

    for row in rows:
        for idx, cell in enumerate(row):
            lens[idx] = max(lens[idx], len(str(cell)))

    header = [
        "  ".join(f"{hdr:<{ln}s}" for ln, hdr in zip(lens, headers)),
        "  ".join("-" * ln for ln in lens),
    ]

    content = [
        "  ".join(f"{c!s:>{ln}s}" for ln, c in zip(lens, r)) for r in rows
    ]

    return "\n".join(header + content)


def write_solution(where: Path, data: ProblemData, result: Result):
    with open(where, "w") as fh:
        if data.num_vehicle_types == 1:
            fh.write(str(result.best))
            fh.write(f"Cost: {round(result.cost(), 2)}\n")
            return

        # Since there are multiple vehicle types, we need to take some care
        # to assign the routes to the proper vehicle. We print all routes,
        # including empty ones. The route indices correspond to the vehicles.
        type2vehicle = [
            (int(vehicle) - 1 for vehicle in vehicle_type.name.split(","))
            for vehicle_type in data.vehicle_types()
        ]

        routes = [f"Route {idx + 1}: " for idx in range(data.num_vehicles)]
        for route in result.best.get_routes():
            visits = map(str, route.visits())
            vehicle = next(type2vehicle[route.vehicle_type()])
            routes[vehicle] += " ".join(visits)

        fh.writelines(route + "\n" for route in routes)
        fh.write(f"Cost: {round(result.cost(), 2)}\n")


def solve(
    data_loc: Path,
    instance_format: str,
    round_func: str,
    seed: int,
    max_runtime: Optional[float],
    max_iterations: Optional[int],
    no_improvement: Optional[int],
    stats_dir: Optional[Path],
    sol_dir: Optional[Path],
    **kwargs,
) -> tuple[str, str, float, int, float]:
    """
    Solves a single VRPLIB instance.

    Parameters
    ----------
    data_loc
        Filesystem location of the VRPLIB instance.
    instance_format
        Data format of the filesystem instance. Argument is passed to
        ``read()``.
    round_func
        Rounding function to use for rounding non-integral data. Argument is
        passed to ``read()``.
    seed
        Seed to use for the RNG.
    max_runtime
        Maximum runtime (in seconds) for solving.
    max_iterations
        Maximum number of iterations for solving.
    no_improvement
        Maximum number of iterations without improvement.
    stats_dir
        The directory to write runtime statistics to.
    sol_dir
        The directory to write the best found solutions to.

    Returns
    -------
    tuple[str, str, float, int, float]
        A tuple containing the instance name, whether the solution is feasible,
        the solution cost, the number of iterations, and the runtime.
    """
    if kwargs.get("config_loc"):
        with open(kwargs["config_loc"], "rb") as fh:
            config = tomli.load(fh)
    else:
        config = {}

    gen_params = GeneticAlgorithmParams(**config.get("genetic", {}))
    pen_params = PenaltyParams(**config.get("penalty", {}))
    pop_params = PopulationParams(**config.get("population", {}))
    nb_params = NeighbourhoodParams(**config.get("neighbourhood", {}))

    data = read(data_loc, instance_format, round_func)
    rng = RandomNumberGenerator(seed=seed)
    pen_manager = PenaltyManager(pen_params)
    pop = Population(bpd, params=pop_params)

    neighbours = compute_neighbours(data, nb_params)
    ls = LocalSearch(data, rng, neighbours)

    node_ops = NODE_OPERATORS
    if "node_ops" in config:
        node_ops = [getattr(pyvrp.search, op) for op in config["node_ops"]]

    for node_op in node_ops:
        ls.add_node_operator(node_op(data))

    route_ops = ROUTE_OPERATORS
    if "route_ops" in config:
        route_ops = [getattr(pyvrp.search, op) for op in config["route_ops"]]

    for route_op in route_ops:
        ls.add_route_operator(route_op(data))

    init = [
        Solution.make_random(data, rng) for _ in range(pop_params.min_pop_size)
    ]
    algo = GeneticAlgorithm(
        data, pen_manager, rng, pop, ls, srex, init, gen_params
    )

    criteria = [
        MaxIterations(max_iterations) if max_iterations is not None else None,
        NoImprovement(no_improvement) if no_improvement is not None else None,
        MaxRuntime(max_runtime) if max_runtime is not None else None,
    ]
    stop = MultipleCriteria([crit for crit in criteria if crit is not None])

    result = algo.run(stop)
    instance_name = data_loc.stem

    if stats_dir:
        stats_dir.mkdir(parents=True, exist_ok=True)  # just in case
        result.stats.to_csv(stats_dir / (instance_name + ".csv"))

    if sol_dir:
        sol_dir.mkdir(parents=True, exist_ok=True)  # just in case
        write_solution(sol_dir / (instance_name + ".sol"), data, result)

    return (
        instance_name,
        "Y" if result.is_feasible() else "N",
        round(result.cost(), 2),
        result.num_iterations,
        round(result.runtime, 3),
    )


def benchmark(instances: list[Path], num_procs: int = 1, **kwargs):
    """
    Solves a list of instances, and prints a table with the results. Any
    additional keyword arguments are passed to ``solve()``.

    Parameters
    ----------
    instances
        Paths to the VRPLIB instances to solve.
    num_procs
        Number of processors to use. Default 1.
    kwargs
        Any additional keyword arguments to pass to the solving function.
    """
    func = partial(solve, **kwargs)
    args = sorted(instances)

    if len(instances) == 1 or num_procs == 1:
        res = [func(arg) for arg in tqdm(args, unit="instance")]
    else:
        res = process_map(func, args, max_workers=num_procs, unit="instance")

    dtypes = [
        ("inst", "U37"),
        ("ok", "U1"),
        ("obj", float),
        ("iters", int),
        ("time", float),
    ]

    data = np.asarray(res, dtype=dtypes)
    headers = ["Instance", "OK", "Obj.", "Iters. (#)", "Time (s)"]

    print("\n", tabulate(headers, data), "\n", sep="")
    print(f"      Avg. objective: {data['obj'].mean():.0f}")
    print(f"     Avg. iterations: {data['iters'].mean():.0f}")
    print(f"   Avg. run-time (s): {data['time'].mean():.2f}")
    print(f"        Total not OK: {np.count_nonzero(data['ok'] == 'N')}")


def main():
    description = """
    This program is a command line interface for solving VRPs, specified in
    VRPLIB format. The program can solve one or multiple such VRP instances,
    and outputs useful information in either case.
    """
    parser = argparse.ArgumentParser(prog="pyvrp", description=description)

    msg = "One or more paths to the VRPLIB instance(s) to solve."
    parser.add_argument("instances", nargs="+", type=Path, help=msg)

    msg = """
    Directory to store runtime statistics in, as CSV files (one per instance).
    """
    parser.add_argument("--stats_dir", type=Path, help=msg)

    msg = """
    Directory to store best observed solutions in, in VRPLIB format (one file
    per instance).
    """
    parser.add_argument("--sol_dir", type=Path, help=msg)

    parser.add_argument(
        "--instance_format",
        default="vrplib",
        choices=INSTANCE_FORMATS,
        help="File format. Default 'vrplib'.",
    )

    parser.add_argument(
        "--round_func",
        default="none",
        choices=ROUND_FUNCS.keys(),
        help="Round function to apply for non-integral data. Default 'none'.",
    )

    msg = """
    Optional parameter configuration file (in TOML format). These arguments
    replace the defaults if a file is passed; default parameters are used when
    this argument is not given.
    """
    parser.add_argument("--config_loc", type=Path, help=msg)

    msg = "Seed to use for reproducible results."
    parser.add_argument("--seed", required=True, type=int, help=msg)

    msg = "Number of processors to use for solving instances. Default 1."
    parser.add_argument("--num_procs", type=int, default=1, help=msg)

    stop = parser.add_argument_group("Stopping criteria")

    msg = "Maximum runtime for each instance, in seconds."
    stop.add_argument("--max_runtime", type=float, help=msg)

    msg = "Maximum number of iterations for solving each instance."
    stop.add_argument("--max_iterations", type=int, help=msg)

    msg = "Maximum number of iterations without improvement."
    stop.add_argument("--no_improvement", type=int, help=msg)

    benchmark(**vars(parser.parse_args()))


if __name__ == "__main__":
    main()
