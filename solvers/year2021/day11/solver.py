from typing import Iterator, Optional
from util import *


def flash(grid: list[list[int]], pos: Vector[int], flashed: set[Vector[int]]):
    if pos in flashed:
        return
    flashed.add(pos)

    for adj in pos.adjacent(include_corners=True):
        if adj not in BoundingBox.from_grid(grid):
            continue
        grid[adj[0]][adj[1]] += 1
        if grid[adj[0]][adj[1]] > 9:
            flash(grid, adj, flashed)


def take_step(grid: list[list[int]]):
    flashed = set[Vector[int]]()
    bbox = BoundingBox.from_grid(grid)
    for pos in bbox.integral_points():
        grid[pos[0]][pos[1]] += 1
    for pos in bbox.integral_points():
        if grid[pos[0]][pos[1]] > 9:
            flash(grid, pos, flashed)
    for pos in flashed:
        grid[pos[0]][pos[1]] = 0
    return flashed


def solve(input: Optional[str]) -> Iterator[any]:
    original_grid = [[int(level) for level in row] for row in input.split("\n")]

    grid = [list(row) for row in original_grid]
    step = 1
    total_flashed = 0
    while step <= 100:
        total_flashed += len(take_step(grid))
        step += 1
    yield total_flashed

    grid = [list(row) for row in original_grid]
    step = 1
    while True:
        if len(take_step(grid)) == sum(len(row) for row in grid):
            yield step
            break
        step += 1
