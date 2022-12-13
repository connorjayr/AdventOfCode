from typing import Iterator, Optional
from util import *


def bfs(grid: list[str], starts: list[tuple[int, int]]) -> int:
    visited = set(starts)
    queue = [(0, pos) for pos in starts]
    while len(queue) > 0:
        steps, pos = queue.pop(0)
        elev = grid[pos[0]][pos[1]]
        if elev == "E":
            return steps
        for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if (
                new_pos[0] < 0
                or new_pos[0] >= len(grid)
                or new_pos[1] < 0
                or new_pos[1] >= len(grid[new_pos[0]])
            ):
                continue
            if new_pos in visited:
                continue
            if elev == "S":
                elev = "a"
            new_elev = grid[new_pos[0]][new_pos[1]]
            if new_elev == "E":
                new_elev = "z"
            if ord(new_elev) - ord(elev) <= 1:
                visited.add(new_pos)
                queue.append((steps + 1, new_pos))


def solve(input: Optional[str]) -> Iterator[any]:
    grid = input.split("\n")
    start_pos: Optional[tuple[int, int]] = None
    starts: list[tuple[int, int]] = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "S" or grid[row][col] == "a":
                if grid[row][col] == "S":
                    start_pos = (row, col)
                starts.append((row, col))
    yield bfs(grid, [start_pos])
    yield bfs(grid, starts)
