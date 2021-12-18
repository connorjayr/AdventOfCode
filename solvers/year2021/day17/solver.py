from typing import Iterator, Optional
from util import *


def is_in_target(vel, target):
    max_height = -math.inf
    pos = (0, 0)
    while pos[1] >= target[1][0]:
        pos = (pos[0] + vel[0], pos[1] + vel[1])
        max_height = max(max_height, pos[1])
        if vel[0] > 0:
            vel = (vel[0] - 1, vel[1] - 1)
        elif vel[0] < 0:
            vel = (vel[0] + 1, vel[1] - 1)
        else:
            vel = (vel[0], vel[1] - 1)

        if (
            target[0][0] <= pos[0]
            and pos[0] <= target[0][1]
            and target[1][0] <= pos[1]
            and pos[1] <= target[1][1]
        ):
            return (True, max_height)
    return (False, max_height)


def solve(input: Optional[str]) -> Iterator[any]:
    pos = (0, 0)
    target = ((201, 230), (-99, -65))
    max_max = -math.inf
    vels = set()
    for y_vel in range(-100, 101):
        print(y_vel)
        for x_vel in range(231):
            in_target, max_height = is_in_target((x_vel, y_vel), target)
            if in_target:
                max_max = max(max_max, max_height)
                vels.add((x_vel, y_vel))
    yield max_max
    yield len(vels)
