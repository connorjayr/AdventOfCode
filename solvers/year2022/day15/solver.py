import re
from typing import Iterator, Optional
from util import *
import z3


SensorBeaconPair = tuple[tuple[int, int], tuple[int, int]]


def cannot_have_beacon(pos: tuple[int, int], pairs: list[SensorBeaconPair]) -> bool:
    for pair in pairs:
        sensor, beacon = pair
        if pos == beacon:
            return False
        dist_to_pos = abs(pos[0] - sensor[0]) + abs(pos[1] - sensor[1])
        dist_to_beacon = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
        if dist_to_pos <= dist_to_beacon:
            return True
    return False


def z3_abs(x: z3.Int):
    return z3.If(x >= 0, x, -x)


def solve(input: Optional[str], is_example: bool) -> Iterator[any]:
    pairs: list[SensorBeaconPair] = []
    for line in input.split("\n"):
        x_sensor, y_sensor, x_beacon, y_beacon = (
            int(coord) for coord in re.findall(r"-?\d+", line)
        )
        pairs.append(((x_sensor, y_sensor), (x_beacon, y_beacon)))

    Y = 2000000 if not is_example else 10
    bbox = None
    for pair in pairs:
        sensor, beacon = pair
        # Radius of the diamond shape at Y
        radius = (
            abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1]) - abs(sensor[1] - Y)
        )
        if radius >= 0:
            if bbox is None:
                bbox = BoundingBox(
                    Vector(sensor[0] - radius, Y), Vector(sensor[0] + radius, Y)
                )
            else:
                bbox.expand(Vector(sensor[0] - radius, Y))
                bbox.expand(Vector(sensor[0] + radius, Y))
    yield [cannot_have_beacon(pos, pairs) for pos in bbox.integral_points()].count(True)

    x = z3.Int("x")
    y = z3.Int("y")

    solver = z3.Solver()

    solver.add(x >= 0)
    solver.add(y >= 0)

    MAX = 4000000 if not is_example else 20
    solver.add(x <= MAX)
    solver.add(y <= MAX)

    for pair in pairs:
        sensor, beacon = pair
        radius = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
        solver.add(z3_abs(x - sensor[0]) + z3_abs(y - sensor[1]) > radius)

    solver.check()
    model = solver.model()
    yield model[x].as_long() * 4000000 + model[y].as_long()
