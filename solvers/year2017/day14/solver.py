import functools
import networkx as nx
import operator
from typing import Iterator, Optional
from util import *


def hash(s: str) -> list[int]:
    nums = list(range(256))
    current_pos = 0
    skip_size = 0
    for _ in range(64):
        for length in [ord(c) for c in s] + [17, 31, 73, 47, 23]:
            for offset in range(length // 2):
                i = (current_pos + offset) % len(nums)
                j = (current_pos + length - offset - 1) % len(nums)
                nums[i], nums[j] = nums[j], nums[i]
            current_pos = (current_pos + length + skip_size) % len(nums)
            skip_size += 1
    dense_hash = [
        functools.reduce(operator.xor, nums[idx : idx + 16])
        for idx in range(0, len(nums), 16)
    ]
    return "".join(hex(num)[2:].rjust(2, "0") for num in dense_hash)


def hex_to_binary(hex: str) -> str:
    return "".join(bin(int(c, 16))[2:].rjust(4, "0") for c in hex)


def solve(input: Optional[str]) -> Iterator[any]:
    grid = [list(hex_to_binary(hash(f"{input}-{row}"))) for row in range(128)]

    yield sum(row.count("1") for row in grid)

    graph = nx.Graph()
    bbox = BoundingBox.from_grid(grid)
    for pos in bbox.integral_points():
        if grid[pos[0]][pos[1]] == "1":
            graph.add_node(pos)
            for neighbor in pos.neighbors(in_bbox=bbox):
                if grid[neighbor[0]][neighbor[1]] == "1":
                    graph.add_edge(pos, neighbor)
    yield nx.number_connected_components(graph)
