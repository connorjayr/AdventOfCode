import functools
import operator
from typing import Iterator, Optional
from util import *


def hash(lengths: int, rounds: int = 1) -> list[int]:
    nums = list(range(256))
    current_pos = 0
    skip_size = 0
    for _ in range(rounds):
        for length in lengths:
            for offset in range(length // 2):
                i = (current_pos + offset) % len(nums)
                j = (current_pos + length - offset - 1) % len(nums)
                nums[i], nums[j] = nums[j], nums[i]
            current_pos = (current_pos + length + skip_size) % len(nums)
            skip_size += 1
    return nums


def solve(input: Optional[str]) -> Iterator[any]:
    nums = hash([int(length) for length in input.split(",")])
    yield nums[0] * nums[1]

    nums = hash([ord(c) for c in input] + [17, 31, 73, 47, 23], 64)
    dense_hash = [
        functools.reduce(operator.xor, nums[idx : idx + 16])
        for idx in range(0, len(nums), 16)
    ]
    yield "".join(hex(num)[2:].rjust(2, "0") for num in dense_hash)
