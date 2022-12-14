from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    grid = {}
    for lines in input.split("\n"):
        endpoints = lines.split(" -> ")
        for idx in range(len(endpoints) - 1):
            x1, y1 = endpoints[idx].split(",")
            x2, y2 = endpoints[idx + 1].split(",")
            for point in Line(
                Vector(int(x1), int(y1)), Vector(int(x2), int(y2))
            ).integral_points():
                grid[(point[0], point[1])] = "#"
    max_y = max(pt[1] for pt in grid.keys())
    sand_before_abyss: Optional[int] = None
    while (500, 0) not in grid:
        pos = (500, 0)
        while True:
            if (pos[0], pos[1] + 1) not in grid and pos[1] + 1 < max_y + 2:
                pos = (pos[0], pos[1] + 1)
            elif (pos[0] - 1, pos[1] + 1) not in grid and pos[1] + 1 < max_y + 2:
                pos = (pos[0] - 1, pos[1] + 1)
            elif (pos[0] + 1, pos[1] + 1) not in grid and pos[1] + 1 < max_y + 2:
                pos = (pos[0] + 1, pos[1] + 1)
            else:
                grid[(pos[0], pos[1])] = "o"
                break
            if pos[1] >= max_y and sand_before_abyss is None:
                sand_before_abyss = list(grid.values()).count("o")
    yield sand_before_abyss
    yield list(grid.values()).count("o")
