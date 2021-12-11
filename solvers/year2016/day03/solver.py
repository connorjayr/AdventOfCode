from typing import Iterator, Optional
from util import *


def is_possible_triangle(a: int, b: int, c: int) -> bool:
    """Determines if a triangle can have the given side lengths.

    Args:
        a: The first side length.
        b: The second side length.
        c: The third side length.

    Returns:
        If a triangle can have side lengths `a`, `b`, and `c`.
    """
    return a + b > c and b + c > a and c + a > b


def solve(input: Optional[str]) -> Iterator[any]:
    triangles = [
        [int(side) for side in triangle.split()] for triangle in input.split("\n")
    ]
    yield sum(is_possible_triangle(*triangle) for triangle in triangles)

    rearranged_triangles = [
        triangle
        for idx in range(0, len(triangles), 3)
        for triangle in zip(*triangles[idx : idx + 3])
    ]
    yield sum(is_possible_triangle(*triangle) for triangle in rearranged_triangles)
