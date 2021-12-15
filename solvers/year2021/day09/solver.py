from collections import deque
from dataclasses import dataclass
from typing import Iterator, Optional
from util import *


@dataclass
class Heightmap:
    heights: list[list[int]]
    bbox: BoundingBox[int]

    def __init__(self, heights):
        self.heights = heights
        self.bbox = BoundingBox(
            Vector[int](0, 0), Vector[int](len(heights) - 1, len(heights[0]) - 1)
        )


def bfs(heightmap: Heightmap, pos: Vector[int], visited: set[Vector[int]]):
    if heightmap.heights[pos[0]][pos[1]] == 9:
        return 0
    queue = deque[Vector[int]]((pos,))
    visited.add(pos)
    size = 0
    while len(queue) > 0:
        head = queue.popleft()
        size += 1
        for neighbor in head.neighbors(in_bbox=heightmap.bbox):
            if neighbor in visited or heightmap.heights[neighbor[0]][neighbor[1]] == 9:
                continue
            queue.append(neighbor)
            visited.add(neighbor)
    return size


def solve(input: Optional[str]) -> Iterator[any]:
    heightmap = Heightmap(
        [[int(height) for height in row] for row in input.split("\n")]
    )

    yield sum(
        heightmap.heights[pos[0]][pos[1]] + 1
        for pos in heightmap.bbox.integral_points()
        if all(
            heightmap.heights[pos[0]][pos[1]]
            < heightmap.heights[neighbor[0]][neighbor[1]]
            for neighbor in pos.neighbors(in_bbox=heightmap.bbox)
        )
    )

    basin_sizes = list[int]()
    visited = set[Vector[int]]()
    for pos in heightmap.bbox.integral_points():
        basin_sizes.append(bfs(heightmap, pos, visited))
    basin_sizes.sort(reverse=True)
    yield basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
