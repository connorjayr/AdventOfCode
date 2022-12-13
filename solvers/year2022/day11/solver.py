from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass
import re
from typing import Iterator, Optional
from util import *


@dataclass
class Monkey:
    items: list[int]
    op: str
    test: int
    on_true: int
    on_false: int


def run_rounds(monkeys: list[Monkey], num_rounds: int, div_by_3=True) -> int:
    lcm = math.lcm(*(monkey.test for monkey in monkeys))
    times_inspected = defaultdict(int)
    for _ in range(num_rounds):
        for idx, monkey in enumerate(monkeys):
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                times_inspected[idx] += 1
                item = eval(monkey.op.replace("old", str(item)))
                if div_by_3:
                    item //= 3
                item %= lcm
                monkeys[
                    monkey.on_true if item % monkey.test == 0 else monkey.on_false
                ].items.append(item)
    times_inspected = sorted(times_inspected.values())
    return times_inspected[-1] * times_inspected[-2]


def solve(input: Optional[str]) -> Iterator[any]:
    monkeys: list[Monkey] = []
    for monkey in input.split("\n\n"):
        monkey = monkey.split("\n")
        items = [int(item) for item in re.findall(r"\d+", monkey[1])]
        op = re.fullmatch(r"  Operation: new = (.+)", monkey[2]).group(1)
        test = int(re.fullmatch(r"  Test: divisible by (\d+)", monkey[3]).group(1))
        on_true = int(
            re.fullmatch(r"    If true: throw to monkey (\d+)", monkey[4]).group(1)
        )
        on_false = int(
            re.fullmatch(r"    If false: throw to monkey (\d+)", monkey[5]).group(1)
        )
        monkeys.append(Monkey(items, op, test, on_true, on_false))

    yield run_rounds(deepcopy(monkeys), 20, True)
    yield run_rounds(deepcopy(monkeys), 10000, False)
