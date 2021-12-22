from collections import Counter
import re
from typing import Iterator, Optional
from util import *


Step = tuple[str, int, int, int, int, int, int]


def run_steps(steps: list[Step]) -> int:
    cuboids = Counter[BoundingBox[int]]()
    for step in steps:
        action, x1, x2, y1, y2, z1, z2 = step
        bbox = BoundingBox[int](
            Vector[int](int(x1), int(y1), int(z1)),
            Vector[int](int(x2), int(y2), int(z2)),
        )

        intersections = Counter[BoundingBox[int]]()
        for other, sign in cuboids.items():
            intersection = bbox & other
            if intersection is not None:
                intersections[intersection] -= sign
        cuboids.update(intersections)
        if action == "on":
            cuboids[bbox] += 1
    return sum(
        (cuboid.upper[0] - cuboid.lower[0] + 1)
        * (cuboid.upper[1] - cuboid.lower[1] + 1)
        * (cuboid.upper[2] - cuboid.lower[2] + 1)
        * sign
        for cuboid, sign in cuboids.items()
    )


def solve(input: Optional[str]) -> Iterator[any]:
    steps = list[Step]()
    for line in input.split("\n"):
        if match := re.fullmatch(
            r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)",
            line,
        ):
            action, x1, x2, y1, y2, z1, z2 = match.groups()
            steps.append((action, int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)))
        else:
            raise InputError(f'unknown command "{line}"')

    yield run_steps([step for step in steps if abs(step[1]) <= 50])
    yield run_steps(steps)
