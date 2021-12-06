from collections import defaultdict
from dataclasses import dataclass
import re
from typing import Iterator, Optional
from util import *


@dataclass
class Destination:
    type: str
    num: int


@dataclass
class GiveInstruction:
    low: Destination
    high: Destination


def parse_instructions(
    lines: list[str],
) -> tuple[list[tuple[int, int]], dict[int, GiveInstruction]]:
    input_instructions = list[tuple[int, int]]()
    give_instructions = dict[int, GiveInstruction]()

    for instruction in lines:
        if match := re.fullmatch(r"value (\d+) goes to bot (\d+)", instruction):
            value, bot = match.groups()
            input_instructions.append((int(bot), int(value)))
        elif match := re.fullmatch(
            r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)",
            instruction,
        ):
            bot, low_type, low_num, high_type, high_num = match.groups()
            give_instructions[int(bot)] = GiveInstruction(
                Destination(low_type, int(low_num)),
                Destination(high_type, int(high_num)),
            )
        else:
            raise InputError(f'unknown instruction "{instruction}"')

    return input_instructions, give_instructions


def give_value(
    bots: defaultdict[int, list[int]],
    outputs: dict[int, int],
    dest: Destination,
    val: int,
):
    if dest.type == "bot":
        bots[dest.num].append(val)
    elif dest.type == "output":
        outputs[dest.num] = val
    else:
        raise InputError(f'unknown destination type "{dest.type}"')


def solve(input: Optional[str]) -> Iterator[any]:
    input_instructions, give_instructions = parse_instructions(input.split("\n"))
    bots = defaultdict[int, list[int]](list[int])
    outputs = dict[int, int]()

    for bot, val in input_instructions:
        bots[bot].append(val)

    while True:
        ready = [
            (bot, vals)
            for bot, vals in bots.items()
            if bot in give_instructions and len(vals) >= 2
        ]
        if len(ready) == 0:
            break

        for bot, vals in ready:
            instruction = give_instructions[bot]

            low_val = min(vals)
            give_value(bots, outputs, instruction.low, low_val)

            high_val = max(vals)
            give_value(bots, outputs, instruction.high, high_val)

            if low_val == 17 and high_val == 61:
                yield bot

            bots[bot] = [val for val in vals if val != low_val and val != high_val]

    yield outputs[0] * outputs[1] * outputs[2]
