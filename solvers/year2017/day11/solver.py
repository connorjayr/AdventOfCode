import math
from typing import Iterator, Optional
from util import *


STEPS = {
    "n": Vector[int](0, 2),
    "ne": Vector[int](1, 1),
    "se": Vector[int](1, -1),
    "s": Vector[int](0, -2),
    "sw": Vector[int](-1, -1),
    "nw": Vector[int](-1, 1),
}


def dist(pos: Vector[int]) -> int:
    if pos[0] > pos[1]:
        return abs(pos[0])
    else:
        return abs(pos[0]) + (abs(pos[1]) - abs(pos[0])) // 2


def solve(input: Optional[str]) -> Iterator[any]:
    pos = Vector[int](0, 0)
    max_dist = -math.inf
    for direction in input.split(","):
        pos += STEPS[direction]
        max_dist = max(max_dist, dist(pos))
    yield dist(pos)
    yield max_dist
