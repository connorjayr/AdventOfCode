from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    sacks = input.split("\n")
    sum_p1 = 0
    sum_p2 = 0
    for idx in range(len(sacks)):
        sack = sacks[idx]
        shared = next(iter(set(sack[: len(sack) // 2]) & set(sack[len(sack) // 2 :])))
        if shared.isupper():
            sum_p1 += ord(shared) - ord("A") + 27
        else:
            sum_p1 += ord(shared) - ord("a") + 1

        if idx % 3 == 0:
            shared = next(
                iter(set(sacks[idx]) & set(sacks[idx + 1]) & set(sacks[idx + 2]))
            )
            if shared.isupper():
                sum_p2 += ord(shared) - ord("A") + 27
            else:
                sum_p2 += ord(shared) - ord("a") + 1
    yield sum_p1
    yield sum_p2
