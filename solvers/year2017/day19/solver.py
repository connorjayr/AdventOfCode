from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    diagram = input.split("\n")

    letters = ""

    pos: Optional[Vector[int]] = None
    for col in range(len(diagram[0])):
        if diagram[0][col] == "|":
            pos = Vector[int](0, col)
            dir = Vector[int](1, 0)
    if pos is None:
        raise InputError("starting position not found")

    while True:
        print(pos)
        if diagram[pos[0]][pos[1]].isalpha():
            letters += diagram[pos[0]][pos[1]]

        moved = False

        straight = pos + dir
        if diagram[straight[0]][straight[1]] != " ":
            pos = straight
            moved = True

        for neighbor in pos.neighbors():
            if diagram[neighbor[0]][neighbor[1]] != " ":
                dir = neighbor - pos
                print(dir)
                pos = neighbor
                moved = True

        if not moved:
            break

    yield letters
