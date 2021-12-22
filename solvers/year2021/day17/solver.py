import re
from typing import Iterator, Optional
from util import *


def is_in_target(vel: Vector[int], target: BoundingBox[int]) -> tuple[bool, int]:
    max_height = -math.inf
    pos = Vector[int](0, 0)
    while pos[0] <= target.upper[0] and pos[1] >= target.lower[1]:
        pos += vel
        max_height = max(max_height, pos[1])

        x_vel = vel[0]
        if x_vel > 0:
            x_vel -= 1
        elif x_vel < 0:
            x_vel += 1
        vel = Vector[int](x_vel, vel[1] - 1)

        if pos in target:
            return (True, max_height)

    return (False, max_height)


def solve(input: Optional[str]) -> Iterator[any]:
    x1, x2, y1, y2 = re.match(
        r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)", input
    ).groups()
    target = BoundingBox[int](
        Vector[int](int(x1), int(y1)), Vector[int](int(x2), int(y2))
    )

    highest_y_pos = -math.inf
    vels = set[Vector[int]]()
    for y_vel in range(target.lower[1], -target.lower[1] + 1):
        for x_vel in range(target.upper[0] + 1):
            vel = Vector[int](x_vel, y_vel)
            in_target, max_height = is_in_target(vel, target)
            if in_target:
                highest_y_pos = max(highest_y_pos, max_height)
                vels.add(vel)
    yield highest_y_pos
    yield len(vels)
