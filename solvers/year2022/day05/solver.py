import copy
import re
from typing import Iterator, Optional
from util import *


def do_procedure(
    initial_stacks: list[list[int]],
    procedure: list[tuple[int, int, int]],
    maintain_order: bool,
) -> list[list[int]]:
    stacks = copy.deepcopy(initial_stacks)
    for amount, source, dest in procedure:
        move = stacks[source - 1][-amount:]
        if not maintain_order:
            move.reverse()
        stacks[dest - 1] += move
        del stacks[source - 1][-amount:]
    return stacks


def solve(input: Optional[str]) -> Iterator[any]:
    starting_stacks, procedure = (group.split("\n") for group in input.split("\n\n"))

    stacks: list[list[str]] = [[] for _ in range(9)]
    for line in starting_stacks[:-1]:
        for col in range(9):
            idx = 4 * col + 1
            if idx < len(line) and line[idx] != " ":
                stacks[col].append(line[idx])
    for stack in stacks:
        stack.reverse()

    procedure = [
        [
            int(n)
            for n in re.fullmatch(
                r"move (\d+) from (\d+) to (\d+)", instruction
            ).groups()
        ]
        for instruction in procedure
    ]

    yield "".join(col[-1] for col in do_procedure(stacks, procedure, False))
    yield "".join(col[-1] for col in do_procedure(stacks, procedure, True))
