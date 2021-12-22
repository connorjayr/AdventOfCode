from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    yield sum(int(digit) for idx, digit in enumerate(input) if input[idx - 1] == digit)
    yield sum(
        int(digit)
        for idx, digit in enumerate(input)
        if input[idx - len(input) // 2] == digit
    )
