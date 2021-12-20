from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    convert_str, input_img = input.split("\n\n")
    input_img = [list(row) for row in input_img.split("\n")]

    output_img = dict[Vector[int], bool]()
    for pos in BoundingBox.from_grid(input_img).integral_points():
        output_img[pos] = input_img[pos[0]][pos[1]] == "#"

    for round in range(1, 51):
        new_img = dict[Vector[int], bool]()
        for pos in (
            BoundingBox.from_vectors(output_img.keys()).extend(2).integral_points()
        ):
            convert_idx = ""
            for neighbor in sorted(
                pos.neighbors(include_diagonal=True, include_self=True), key=tuple
            ):
                convert_idx += "1" if output_img.get(neighbor, round % 2 == 0) else "0"
            new_img[pos] = convert_str[int(convert_idx, 2)] == "#"
        output_img = new_img
        if round in (2, 50):
            yield sum(output_img.values())
