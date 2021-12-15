from typing import Iterator, Optional
from util import *
import networkx as nx


def find_path(cave: list[list[int]]) -> int:
    graph = nx.DiGraph()
    bbox = BoundingBox.from_grid(cave)
    for pos in bbox.integral_points():
        for neighbor in pos.neighbors(in_bbox=bbox):
            graph.add_edge(neighbor, pos, weight=cave[pos[0]][pos[1]])
    return nx.dijkstra_path_length(graph, bbox.lower, bbox.upper)


def solve(input: Optional[str]) -> Iterator[any]:
    cave = [[int(level) for level in row] for row in input.split("\n")]
    yield find_path(cave)

    full_cave = []
    for row in range(len(cave) * 5):
        full_row = []
        for col in range(len(cave[0] * 5)):
            offset = row // len(cave) + col // len(cave[0])
            base_level = cave[row % len(cave)][col % len(cave[0])]
            full_row.append((base_level + offset - 1) % 9 + 1)
        full_cave.append(full_row)
    yield find_path(full_cave)
