from dataclasses import dataclass
import itertools
from typing import Iterator, Optional
from util import *


DIGITS = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]


@dataclass
class Entry:
    inputs: list[str]
    outputs: list[str]


def find_mapping(entry: Entry):
    for mapping in itertools.permutations("abcdefg"):
        mapping = dict(zip(mapping, "abcdefg"))
        valid = True
        for val in entry.inputs + entry.outputs:
            mapped = "".join(sorted(mapping[c] for c in val))
            if mapped not in DIGITS:
                valid = False
                break
        if not valid:
            continue
        return mapping


def solve(input: Optional[str]) -> Iterator[any]:
    entries = list[Entry]()
    for line in input.split("\n"):
        inputs, outputs = line.split(" | ")
        entries.append(Entry(inputs.split(), outputs.split()))

    yield sum(
        sum(len(output) in [2, 4, 3, 7] for output in entry.outputs)
        for entry in entries
    )

    total_outputs = 0
    for entry in entries:
        mapping = find_mapping(entry)
        output = ""
        for digit in entry.outputs:
            output += str(DIGITS.index("".join(sorted(mapping[c] for c in digit))))
        total_outputs += int(output)
    yield total_outputs
