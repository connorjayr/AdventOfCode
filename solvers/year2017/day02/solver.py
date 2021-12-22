from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    checksum = 0
    sum_of_quotients = 0

    for row in input.split("\n"):
        vals = [int(val) for val in row.split()]
        checksum += max(vals) - min(vals)

        for i in range(len(vals)):
            for j in range(len(vals)):
                if i == j:
                    continue
                if vals[i] % vals[j] == 0:
                    sum_of_quotients += vals[i] // vals[j]

    yield checksum
    yield sum_of_quotients
