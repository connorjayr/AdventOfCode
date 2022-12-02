from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    calories_per_elf = sorted(
        sum(int(item) for item in elf.split("\n")) for elf in input.split("\n\n")
    )
    yield calories_per_elf[-1]
    yield sum(calories_per_elf[-3:])
