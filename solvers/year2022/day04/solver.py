import re
from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    count_contains = 0
    count_overlaps = 0
    for line in input.split("\n"):
        start_1, end_1, start_2, end_2 = (int(n) for n in re.findall(r"\d+", line))
        if start_1 <= start_2 <= end_2 <= end_1 or start_2 <= start_1 <= end_1 <= end_2:
            count_contains += 1
        if (
            start_1 <= start_2 <= end_1
            or start_1 <= end_2 <= end_1
            or start_2 <= start_1 <= end_2
            or start_2 <= end_1 <= end_2
        ):
            count_overlaps += 1
    yield count_contains
    yield count_overlaps
