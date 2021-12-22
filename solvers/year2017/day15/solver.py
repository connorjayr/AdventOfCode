from typing import Iterator, Optional
from util import *


def gen(prev: int, factor: int, only_multiples_of: int = 1) -> Iterator[int]:
    while True:
        prev = (prev * factor) % 2147483647
        if prev % only_multiples_of == 0:
            yield prev


def solve(input: Optional[str]) -> Iterator[any]:
    vals = [int(line.split()[-1]) for line in input.split("\n")]

    gen_a = gen(vals[0], 16807)
    gen_b = gen(vals[1], 48271)
    count = 0
    for _ in range(40000000):
        if next(gen_a) & 0b1111111111111111 == next(gen_b) & 0b1111111111111111:
            count += 1
    yield count

    gen_a = gen(vals[0], 16807, only_multiples_of=4)
    gen_b = gen(vals[1], 48271, only_multiples_of=8)
    count = 0
    for _ in range(5000000):
        if next(gen_a) & 0b1111111111111111 == next(gen_b) & 0b1111111111111111:
            count += 1
    yield count
