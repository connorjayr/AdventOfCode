from dataclasses import dataclass
import functools
from networkx import DiGraph
from networkx.algorithms import shortest_path_length
import re
from typing import Iterator, Optional
from util import *


@dataclass
class Valve:
    rate: int
    neighbors: dict[str, int]


VALVES: dict[str, Valve] = {}


@functools.cache
def max_pressure_released(
    remaining_time: int, valve: str, closed: frozenset[str], elephant=False
) -> int:
    result = 0
    for next_valve in closed:
        dist = VALVES[valve].neighbors[next_valve]
        if dist >= remaining_time:
            continue
        result = max(
            result,
            VALVES[next_valve].rate * (remaining_time - dist - 1)
            + max_pressure_released(
                remaining_time - dist - 1, next_valve, closed - {next_valve}, elephant
            ),
        )
    if elephant:
        result = max(result, max_pressure_released(26, "AA", closed))
    return result


def solve(input: Optional[str]) -> Iterator[any]:
    original_valves: dict[str, Valve] = {}
    # Valve AA probably does actually have zero flow, but we would like to know its distance to the
    # other valves
    nonzero_valves = ["AA"]
    original_graph = DiGraph()
    for line in input.split("\n"):
        valve, rate, neighbors = re.fullmatch(
            r"Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (..(?:, ..)*)",
            line,
        ).groups()
        rate = int(rate)
        neighbors = [(dest, 1) for dest in neighbors.split(", ")]

        original_valves[valve] = Valve(rate, neighbors)
        if rate > 0:
            nonzero_valves.append(valve)
        for neighbor, dist in neighbors:
            original_graph.add_edge(valve, neighbor, weight=dist)

    # Perform vertex contraction for all zero flow valves, since we never need to stop at them to
    # open
    for a in nonzero_valves:
        neighbors: dict[str, int] = {}
        for b in nonzero_valves:
            neighbors[b] = shortest_path_length(original_graph, a, b)
        VALVES[a] = Valve(original_valves[a].rate, neighbors)

    yield max_pressure_released(30, "AA", frozenset(VALVES.keys()))
    yield max_pressure_released(26, "AA", frozenset(VALVES.keys()), True)
