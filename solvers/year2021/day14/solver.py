from collections import Counter
from typing import Iterator, Optional
from util import *


def apply_steps(template: str, rules: dict[str, str], steps: int):
    pairs = Counter[str](a + b for a, b in zip(template, template[1:]))

    for _ in range(steps):
        new_pairs = Counter[str]()
        for pair, count in pairs.items():
            if pair in rules:
                new_pairs[pair[0] + rules[pair]] += count
                new_pairs[rules[pair] + pair[1]] += count
        pairs = new_pairs

    letters = Counter[str](template[-1])
    for pair, count in pairs.items():
        letters[pair[0]] += count
    most_common = letters.most_common()
    return most_common[0][1] - most_common[-1][1]


def solve(input: Optional[str]) -> Iterator[any]:
    sections = input.split("\n\n")
    template = sections[0]
    rules = {}
    for rule in sections[1].split("\n"):
        pair, insert = rule.split(" -> ")
        rules[pair] = insert

    yield apply_steps(template, rules, 10)
    yield apply_steps(template, rules, 40)
