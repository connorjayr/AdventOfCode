import math
from typing import Iterator, Optional
from util import *


def divisors_of(n: int, max_quotient=math.inf) -> set[int]:
    divisors = set((n,))
    if n <= max_quotient:
        divisors.add(1)

    for d in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % d == 0:
            if n // d <= max_quotient:
                divisors.add(d)
            if d <= max_quotient:
                divisors.add(n // d)

    return divisors


def solve(input: Optional[str]) -> Iterator[any]:
    min_presents = int(input)

    house_number = 1
    while sum(divisors_of(house_number)) * 10 < min_presents:
        house_number += 1
    yield house_number

    house_number = 1
    while sum(divisors_of(house_number, max_quotient=50)) * 11 < min_presents:
        house_number += 1
    yield house_number
