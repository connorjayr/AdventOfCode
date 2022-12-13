from typing import Iterator, Optional
from util import *

DIRECTIONS = {"R": (1, 0), "U": (0, -1), "D": (0, 1), "L": (-1, 0)}


def sign(n: int) -> int:
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0


def move_rope(length: int, moves: list[str]) -> int:
    rope = [(0, 0) for _ in range(length)]
    tail_visited: set[tuple[int, int]] = set()
    for move in moves:
        direction, steps = move.split(" ")
        d = DIRECTIONS[direction]
        steps = int(steps)
        for _ in range(steps):
            rope[0] = (rope[0][0] + d[0], rope[0][1] + d[1])
            for idx in range(length - 1):
                prev_knot = rope[idx]
                next_knot = rope[idx + 1]
                if (
                    abs(prev_knot[0] - next_knot[0]) > 1
                    or abs(prev_knot[1] - next_knot[1]) > 1
                ):
                    x = next_knot[0] + sign(prev_knot[0] - next_knot[0])
                    y = next_knot[1] + sign(prev_knot[1] - next_knot[1])
                    rope[idx + 1] = (x, y)
            tail_visited.add(rope[-1])
    return len(tail_visited)


def solve(input: Optional[str]) -> Iterator[any]:
    moves = input.split("\n")
    yield move_rope(2, moves)
    yield move_rope(10, moves)
