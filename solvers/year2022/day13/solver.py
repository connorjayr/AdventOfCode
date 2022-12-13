from functools import cmp_to_key
from typing import Iterator, Optional, Union
from util import *


Packet = Union[int, list["Packet"]]


def compare_packets(a: Packet, b: Packet) -> int:
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, list) and isinstance(b, list):
        for idx in range(min(len(a), len(b))):
            result = compare_packets(a[idx], b[idx])
            if result != 0:
                return result
        return len(a) - len(b)
    elif isinstance(a, int):
        return compare_packets([a], b)
    elif isinstance(b, int):
        return compare_packets(a, [b])
    else:
        raise InputError("packet is not an int or list")


def solve(input: Optional[str]) -> Iterator[any]:
    sum_in_order = 0
    all_packets: list[Packet] = []
    for idx, pairs in enumerate(input.split("\n\n")):
        a: Packet = eval(pairs.split("\n")[0])
        b: Packet = eval(pairs.split("\n")[1])
        if compare_packets(a, b) < 0:
            sum_in_order += idx + 1
        all_packets.append(a)
        all_packets.append(b)

    yield sum_in_order

    all_packets.append([[2]])
    all_packets.append([[6]])
    all_packets = sorted(
        all_packets, key=cmp_to_key(lambda a, b: compare_packets(a, b))
    )
    yield (all_packets.index([[2]]) + 1) * (all_packets.index([[6]]) + 1)
