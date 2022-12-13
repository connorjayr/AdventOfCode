from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    instructions = input.split("\n")
    # Index of current instruction and number of cycles it has been running
    curr = (0, 0)

    register = 1
    cycle_num = 1

    signal_strength = 0
    screen = ""
    while cycle_num <= 240:
        curr = (curr[0], curr[1] + 1)

        if cycle_num in (20, 60, 100, 140, 180, 220):
            signal_strength += cycle_num * register
        screen += "█" if abs((cycle_num - 1) % 40 - register) <= 1 else " "

        instruction = instructions[curr[0]]
        if instruction == "noop":
            curr = (curr[0] + 1, 0)
        elif instruction.startswith("addx ") and curr[1] == 2:
            amount = int(instruction.split(" ")[1])
            register += amount
            curr = (curr[0] + 1, 0)

        cycle_num += 1
    yield signal_strength
    yield "\n".join(screen[40 * row : 40 * (row + 1)] for row in range(6))
