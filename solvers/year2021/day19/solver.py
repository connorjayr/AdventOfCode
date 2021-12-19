from collections import deque
from dataclasses import dataclass
from itertools import combinations
from typing import Iterator, Optional
from util import *


@dataclass
class Scanner:
    beacons: set[Vector[int]]
    pos: Optional[Vector[int]] = None


def all_rotations(pos: Vector[int]):
    result = []
    x, y, z = pos

    result.append(Vector[int](x, y, z))
    result.append(Vector[int](y, z, x))
    result.append(Vector[int](z, x, y))
    result.append(Vector[int](z, y, -x))
    result.append(Vector[int](y, x, -z))
    result.append(Vector[int](x, z, -y))

    result.append(Vector[int](x, -y, -z))
    result.append(Vector[int](y, -z, -x))
    result.append(Vector[int](z, -x, -y))
    result.append(Vector[int](z, -y, x))
    result.append(Vector[int](y, -x, z))
    result.append(Vector[int](x, -z, y))

    result.append(Vector[int](-x, y, -z))
    result.append(Vector[int](-y, z, -x))
    result.append(Vector[int](-z, x, -y))
    result.append(Vector[int](-z, y, x))
    result.append(Vector[int](-y, x, z))
    result.append(Vector[int](-x, z, y))

    result.append(Vector[int](-x, -y, z))
    result.append(Vector[int](-y, -z, x))
    result.append(Vector[int](-z, -x, y))
    result.append(Vector[int](-z, -y, -x))
    result.append(Vector[int](-y, -x, -z))
    result.append(Vector[int](-x, -z, -y))

    return result


def determine_pos(a: Scanner, b: Scanner) -> bool:
    for beacons in zip(*(all_rotations(beacon) for beacon in b.beacons)):
        for beacon_from_a in a.beacons:
            for beacon_from_b in beacons[:-11]:
                b_to_a = beacon_from_a - beacon_from_b
                offset_beacons = set(beacon + b_to_a for beacon in beacons)
                if len(a.beacons.intersection(offset_beacons)) >= 12:
                    b.beacons = set(beacons)

                    b.pos = a.pos + b_to_a
                    print(f"Positioned scanner at {b.pos}")

                    return True
    return False


def solve(input: Optional[str]) -> Iterator[any]:
    scanners = list[Scanner]()
    for scanner in input.split("\n\n"):
        beacons = set[Vector[int]]()
        for beacon in scanner.split("\n")[1:]:
            x, y, z = beacon.split(",")
            beacons.add(Vector[int](int(x), int(y), int(z)))
        scanners.append(Scanner(beacons))
    scanners[0].pos = Vector[int](0, 0, 0)

    queue = deque[Scanner]((scanners[0],))
    while len(queue) > 0:
        num_positioned = sum(scanner.pos is not None for scanner in scanners)
        unpositioned = [scanner for scanner in scanners if scanner.pos is None]
        print(f"Positioned {num_positioned} scanner(s), {len(unpositioned)} to go")
        a = queue.popleft()
        for b in unpositioned:
            if determine_pos(a, b):
                queue.append(b)

    all_beacons = set[Vector[int]]()
    for scanner in scanners:
        for beacon in scanner.beacons:
            all_beacons.add(beacon + scanner.pos)
    yield len(all_beacons)

    yield max(
        sum(abs(y - x) for x, y in zip(a.pos, b.pos))
        for a, b in combinations(scanners, 2)
    )
