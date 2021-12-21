import functools
import itertools
from typing import Iterator, Optional
from util import *


@functools.cache
def count_wins(
    spaces: tuple[int, int], scores: tuple[int, int], turn: int
) -> Vector[int]:
    if scores[0] >= 21:
        return (1, 0)
    elif scores[1] >= 21:
        return (0, 1)
    wins = Vector[int](0, 0)
    for rolls in itertools.product((1, 2, 3), repeat=3):
        new_spaces = list[int](spaces)
        new_spaces[turn] = (new_spaces[turn] + sum(rolls) - 1) % 10 + 1

        new_scores = list[int](scores)
        new_scores[turn] += new_spaces[turn]

        wins += count_wins(
            tuple[int, int](new_spaces), tuple[int, int](new_scores), 1 - turn
        )
    return wins


def solve(input: Optional[str]) -> Iterator[any]:
    starting_spaces = [int(line.split()[-1]) for line in input.split("\n")]

    spaces = list(starting_spaces)
    scores = [0, 0]
    dice = 1
    turn = 0
    while all(score < 1000 for score in scores):
        spaces[turn] = (spaces[turn] + 3 * (dice + 1) - 1) % 10 + 1
        scores[turn] += spaces[turn]
        dice += 3
        turn = 1 - turn
    yield min(scores) * (dice - 1)

    yield max(count_wins(tuple(starting_spaces), (0, 0), 0))
