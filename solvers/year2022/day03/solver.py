from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    sacks = input.split("\n")
    sumt = 0
    for i in range(0, len(sacks), 3):
        one = sacks[i]
        two = sacks[i + 1]
        thr = sacks[i + 2]
        # left = set(sack[: len(sack) // 2])
        # right = set(sack[len(sack) // 2 :])
        shared = set(one).intersection(set(two).intersection(set(thr)))
        shared = ord(next(iter(shared)))
        if ord("a") <= shared <= ord("z"):
            sumt += shared - ord("a") + 1
        else:
            sumt += shared - ord("A") + 27
    yield 0
    yield sumt
