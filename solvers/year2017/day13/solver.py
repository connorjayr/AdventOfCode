from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    ranges = dict[int, int]()
    for line in input.split("\n"):
        depth, range = line.split(": ")
        ranges[int(depth)] = int(range)

    total_severity = 0
    for depth, range in ranges.items():
        if depth % (2 * (range - 1)) == 0:
            total_severity += depth * range
    yield total_severity

    delay = 0
    caught = True
    while caught:
        caught = False
        for depth, range in ranges.items():
            if (depth + delay) % (2 * (range - 1)) == 0:
                caught = True
        if caught:
            delay += 1
    yield delay
