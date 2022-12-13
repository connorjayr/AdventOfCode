import math
from typing import Iterator, Optional
from util import *


def is_visible(trees: list[list[int]], pos: tuple[int, int]):
    height = trees[pos[0]][pos[1]]
    row, col = pos
    return (
        all(trees[r][col] < height for r in range(row))
        or all(trees[r][col] < height for r in range(row + 1, len(trees)))
        or all(trees[row][c] < height for c in range(col))
        or all(trees[row][c] < height for c in range(col + 1, len(trees[0])))
    )


def score(trees: list[list[int]], pos: tuple[int, int]):
    height = trees[pos[0]][pos[1]]
    score = 1
    for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        dist = 0
        curr = (pos[0] + d[0], pos[1] + d[1])
        while (
            curr[0] >= 0
            and curr[0] < len(trees)
            and curr[1] >= 0
            and curr[1] < len(trees[curr[0]])
        ):
            dist += 1
            if trees[curr[0]][curr[1]] >= height:
                break
            curr = (curr[0] + d[0], curr[1] + d[1])
        score *= dist
    return score


def solve(input: Optional[str]) -> Iterator[any]:
    trees = [[int(height) for height in row] for row in input.split("\n")]
    num_visible = 0
    max_score = -math.inf
    for row in range(len(trees)):
        for col in range(len(trees[row])):
            if is_visible(trees, (row, col)):
                num_visible += 1
            max_score = max(max_score, score(trees, (row, col)))
    yield num_visible
    yield max_score
