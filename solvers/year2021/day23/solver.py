from collections import deque
import functools
from typing import Iterator, Optional
import sys
from util import *


ROOMS = {"A": 3, "B": 5, "C": 7, "D": 9}
COSTS = {"A": 1, "B": 10, "C": 100, "D": 1000}


HALLWAY = [
    Vector[int](1, 1),
    Vector[int](1, 2),
    Vector[int](1, 4),
    Vector[int](1, 6),
    Vector[int](1, 8),
    Vector[int](1, 10),
    Vector[int](1, 11),
]


def can_move_into_room(burrow: list[list[str]], letter: str) -> Optional[Vector[int]]:
    col = ROOMS[letter]
    if burrow[2][col] != "." or (burrow[3][col] != "." and burrow[3][col] != letter):
        return None
    return Vector[int](3, col) if burrow[3][col] == "." else Vector[int](2, col)


def is_reachable(
    start: Vector[int], end: Vector[int], burrow: list[list[str]]
) -> Optional[int]:
    # visited = set((start,))
    # queue = deque(((0, start),))
    # bbox = BoundingBox.from_grid(burrow)
    # while len(queue) > 0:
    #     length, pos = queue.popleft()
    #     if pos == end:
    #         return length
    #     for neighbor in pos.neighbors(in_bbox=bbox):
    #         if neighbor in visited:
    #             continue
    #         if burrow[neighbor[0]][neighbor[1]] != ".":
    #             continue
    #         visited.add(neighbor)
    #         queue.append((length + 1, neighbor))
    # return None


@functools.cache
def min_cost(burrow: tuple[tuple[str]]) -> int:
    burrow = [list(row) for row in burrow]
    done = True
    for letter, col in ROOMS.items():
        for row in (2, 3):
            if burrow[row][col] != letter:
                done = False
                break
        if not done:
            break
    if done:
        return 0

    poss = [math.inf]
    for pos in HALLWAY:
        c = burrow[pos[0]][pos[1]]
        if c != ".":
            dest = can_move_into_room(burrow, c)
            if dest is None:
                continue
            dist = is_reachable(pos, dest, burrow)
            if dist is None:
                continue
            cost = COSTS[c] * dist
            burrow[dest[0]][dest[1]] = c
            burrow[pos[0]][pos[1]] = "."
            poss.append(cost + min_cost(tuple(tuple(row) for row in burrow)))
            burrow[dest[0]][dest[1]] = "."
            burrow[pos[0]][pos[1]] = c

    for letter, col in ROOMS.items():
        room_done = True
        for row in (2, 3):
            if burrow[row][col] != letter and burrow[row][col] != ".":
                room_done = False
                break
        if room_done:
            continue
        row = 2 if burrow[2][col] != "." else 3
        c = burrow[row][col]
        for dest in HALLWAY:
            if burrow[dest[0]][dest[1]] != ".":
                continue
            dist = is_reachable(Vector[int](row, col), dest, burrow)
            if dist is None:
                continue
            cost = COSTS[letter] * dist
            burrow[dest[0]][dest[1]] = c
            burrow[row][col] = "."
            poss.append(cost + min_cost(tuple(tuple(row) for row in burrow)))
            burrow[dest[0]][dest[1]] = "."
            burrow[row][col] = c

    return min(poss)


def solve(input: Optional[str]) -> Iterator[any]:
    sys.setrecursionlimit(10000)
    burrow = tuple(tuple(row) for row in input.split("\n"))
    yield min_cost(burrow)

