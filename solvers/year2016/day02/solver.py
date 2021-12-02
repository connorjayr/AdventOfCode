from typing import Generator, List, Optional, Union
from util import *


def get_code(
    keypad: Tuple[Tuple[int]],
    keypad_bbox: Union[BoundingBox, List[Vector]],
    start_pos: Vector,
    instructions: List[str],
) -> str:
    code = ""

    pos = start_pos
    dirs = {"U": UP, "R": RIGHT, "D": DOWN, "L": LEFT}
    for line in instructions:
        for dir in line:
            if dir in dirs:
                dest = pos + dirs[dir]
                if dest in keypad_bbox:
                    pos = dest
            else:
                raise InputError(f'unknown direction "{dir}"')
        code += keypad[pos[1]][pos[0]]
    return code


def solve(input: Optional[str]) -> Generator[any, None, None]:
    instructions = input.split("\n")
    yield get_code(
        (("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9")),
        BoundingBox(Vector(0, 0), Vector(2, 2)),
        Vector(1, 1),
        instructions,
    )

    actual_keypad = (
        (" ", " ", "1", " ", " "),
        (" ", "2", "3", "4", " "),
        ("5", "6", "7", "8", "9"),
        (" ", "A", "B", "C", " "),
        (" ", " ", "D", " ", " "),
    )
    actual_keypad_bbox = []
    for y in range(len(actual_keypad)):
        for x in range(len(actual_keypad[y])):
            if actual_keypad[y][x] != " ":
                actual_keypad_bbox.append(Vector(x, y))
    yield get_code(
        actual_keypad,
        actual_keypad_bbox,
        Vector(2, 2),
        instructions,
    )
