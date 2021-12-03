from collections import Counter
from typing import Generator, List, Optional
from util import *


def find_rating(numbers: List[str], most_common: bool) -> int:
    remaining = list(numbers)
    idx = 0
    while len(remaining) > 1:
        bit_counts = Counter(number[idx] for number in remaining)
        if bit_counts["0"] == bit_counts["1"]:
            # Tiebreaker
            bit_criteria = "1" if most_common else "0"
        else:
            bit_criteria = bit_counts.most_common()[0 if most_common else -1][0]
        remaining = [number for number in remaining if number[idx] == bit_criteria]
        idx += 1

    return int(remaining[0], 2)


def solve(input: Optional[str]) -> Generator[any, None, None]:
    numbers = input.split("\n")
    gamma = ""
    epsilon = ""
    for idx in range(len(numbers[0])):
        bit_counts = Counter(number[idx] for number in numbers)
        most_common = bit_counts.most_common()
        gamma += most_common[0][0]
        epsilon += most_common[-1][0]
    yield int(gamma, 2) * int(epsilon, 2)

    yield find_rating(numbers, True) * find_rating(numbers, False)
