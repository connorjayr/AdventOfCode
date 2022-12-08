from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    for marker_len in (4, 14):
        for start_idx in range(len(input) - marker_len + 1):
            if len(set(input[start_idx : start_idx + marker_len])) == marker_len:
                yield start_idx + marker_len
                break
