from typing import Iterator, Optional
from util import *
import math


def solve(input: Optional[str]) -> Iterator[any]:
    positions = [int(pos) for pos in input.split(",")]
    pos_range = range(min(positions), max(positions) + 1)
    yield min(sum(abs(pos - align_pos) for pos in positions) for align_pos in pos_range)
    yield min(
        sum(abs(pos - align_pos) * (abs(pos - align_pos) + 1) // 2 for pos in positions)
        for align_pos in pos_range
    )
