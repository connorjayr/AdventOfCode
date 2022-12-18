from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    cubes: set[Vector[int]] = set()
    for cube in input.split("\n"):
        x, y, z = (int(coord) for coord in cube.split(","))
        cubes.add(Vector(x, y, z))

    surface_area = 0
    for cube in cubes:
        surface_area += [neighbor in cubes for neighbor in cube.neighbors()].count(
            False
        )
    yield surface_area

    exterior = 0
    first_cube = next(iter(cubes))
    bbox: BoundingBox[int] = BoundingBox(first_cube, first_cube)
    for cube in cubes:
        bbox.expand(cube)
    for cube in cubes:
        for neighbor in cube.neighbors():
            if neighbor in cubes:
                continue
            visited: set[Vector[int]] = set((neighbor,))
            queue = [neighbor]
            while len(queue) > 0:
                bfs_cube = queue.pop(0)
                if bfs_cube not in bbox:
                    exterior += 1
                    break
                for bfs_neighbor in bfs_cube.neighbors():
                    if bfs_neighbor in visited or bfs_neighbor in cubes:
                        continue
                    visited.add(bfs_neighbor)
                    queue.append(bfs_neighbor)

    yield exterior
