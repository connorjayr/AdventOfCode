from collections import defaultdict
from typing import Iterator, Optional
from util import *


def solve(input: Optional[str], is_example: bool) -> Iterator[any]:
    elves = set()
    lines = input.split("\n")
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "#":
                elves.add((row, col))
    considers = [
        ((-1, 0), [(-1, -1), (-1, 0), (-1, 1)]),
        ((1, 0), [(1, -1), (1, 0), (1, 1)]),
        ((0, -1), [(-1, -1), (0, -1), (1, -1)]),
        ((0, 1), [(-1, 1), (0, 1), (1, 1)]),
    ]
    round = 1
    while True:
        minRow = min(row for row, _ in elves)
        maxRow = max(row for row, _ in elves)
        minCol = min(col for _, col in elves)
        maxCol = max(col for _, col in elves)
        # for row in range(minRow, maxRow + 1):
        #     for col in range(minCol, maxCol + 1):
        #         print("." if (row, col) not in elves else "#", end="")
        #     print()
        # print()
        newElves = set()
        poss = defaultdict(int)
        moves = []
        for elf in elves:
            moved = False
            surrounded = False
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == 0 and dc == 0:
                        continue
                    if (elf[0] + dr, elf[1] + dc) in elves:
                        surrounded = True
                        break
            if surrounded:
                for d, checks in considers:
                    not_in = 0
                    for check in checks:
                        if (elf[0] + check[0], elf[1] + check[1]) not in elves:
                            not_in += 1
                    if not_in >= 3:
                        moved = True
                        moves.append((elf, (elf[0] + d[0], elf[1] + d[1])))
                        poss[(elf[0] + d[0], elf[1] + d[1])] += 1
                        break
            if not moved:
                newElves.add(elf)

        for move in moves:
            if poss[move[1]] > 1:
                newElves.add(move[0])
                continue
            else:
                assert poss[move[1]] == 1
                newElves.add(move[1])
        if elves == newElves:
            yield round
        elves = newElves
        considers = considers[1:] + [considers[0]]
        round += 1

    minRow = min(row for row, _ in elves)
    maxRow = max(row for row, _ in elves)
    minCol = min(col for _, col in elves)
    maxCol = max(col for _, col in elves)
    empty = 0
    for row in range(minRow, maxRow + 1):
        for col in range(minCol, maxCol + 1):
            if (row, col) not in elves:
                empty += 1
    yield empty
