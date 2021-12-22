from dataclasses import dataclass
from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    step = int(input)

    buffer = [0]
    current_pos = 0
    for val in range(1, 2018):
        current_pos = (current_pos + step) % len(buffer) + 1
        buffer.insert(current_pos, val)
    yield buffer[buffer.index(2017) + 1]

    val_after_0 = 0
    current_pos = 0
    for val in range(1, 50000001):
        current_pos = (current_pos + step) % val + 1
        if current_pos == 1:
            val_after_0 = val
    yield val_after_0
