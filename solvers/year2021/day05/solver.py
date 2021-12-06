from typing import Counter, Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    lines = list[Line]()
    for line in input.split("\n"):
        points = line.split(" -> ")
        x1, y1 = points[0].split(",")
        x2, y2 = points[1].split(",")
        lines.append(Line(Vector[int](int(x1), int(y1)), Vector[int](int(x2), int(y2))))

    diagram = Counter[Vector[int]]()

    # Add the horizontal and vertical lines to the diagram
    straight_lines = [line for line in lines if any(x == 0 for x in line.slope())]
    for line in straight_lines:
        for point in line.integral_points():
            diagram[point] += 1
    yield sum(overlapping_lines >= 2 for overlapping_lines in diagram.values())

    # Add the diagonal lines to the diagram
    diagonal_lines = [line for line in lines if all(x != 0 for x in line.slope())]
    for line in diagonal_lines:
        for point in line.integral_points():
            diagram[point] += 1
    yield sum(overlapping_lines >= 2 for overlapping_lines in diagram.values())
