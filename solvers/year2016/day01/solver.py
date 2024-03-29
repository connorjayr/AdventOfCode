from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    pos = Vector[int](0, 0)
    dir = Vector[int](0, 1)

    visited = set[Vector[int]]()
    first_pos_visited_twice: Optional[Vector[int]] = None

    for instruction in input.split(", "):
        turn = instruction[0]
        dist = int(instruction[1:])
        if turn == "L":
            dir = dir.rotate_ccw()
        elif turn == "R":
            dir = dir.rotate_cw()
        else:
            raise InputError(f'unknown direction "{turn}"')

        for step in range(1, dist + 1):
            dest = pos + step * dir
            if dest in visited and first_pos_visited_twice is None:
                first_pos_visited_twice = dest
            visited.add(dest)

        pos += dist * dir

    yield (sum(abs(x) for x in pos))
    yield (sum(abs(x) for x in first_pos_visited_twice))
