from typing import Iterator, Optional
from util import *


def fold_paper(paper: set[Vector[int]], line: str) -> set[Vector[int]]:
    axis, val = line.split("=")
    val = int(val)

    folded = set[Vector[int]]()
    for dot in paper:
        if axis == "x" and dot[0] > val:
            folded.add(Vector[int](2 * val - dot[0], dot[1]))
        elif axis == "y" and dot[1] > val:
            folded.add(Vector[int](dot[0], 2 * val - dot[1]))
        else:
            folded.add(dot)
    return folded


def display_paper(paper: set[Vector[int]]) -> str:
    s = ""
    for y in range(0, max(pos[1] for pos in paper) + 1):
        for x in range(0, max(pos[0] for pos in paper) + 1):
            s += "#" if (x, y) in paper else " "
        s += "\n"
    return s


def solve(input: Optional[str]) -> Iterator[any]:
    dots, folds = input.split("\n\n")
    paper = set[Vector[int]]()
    for dot in dots.split("\n"):
        x, y = dot.split(",")
        paper.add(Vector[int](int(x), int(y)))

    num_folds = 0
    for fold in folds.split("\n"):
        line = fold.split()[2]
        paper = fold_paper(paper, line)
        num_folds += 1
        if num_folds == 1:
            yield len(paper)
    yield display_paper(paper)
