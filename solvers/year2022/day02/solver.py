from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    score_p1 = 0
    score_p2 = 0
    for round in input.split("\n"):
        round = round.split(" ")
        if round == ["A", "X"]:
            score_p1 += 4
            score_p2 += 3
        elif round == ["A", "Y"]:
            score_p1 += 8
            score_p2 += 4
        elif round == ["A", "Z"]:
            score_p1 += 3
            score_p2 += 8
        elif round == ["B", "X"]:
            score_p1 += 1
            score_p2 += 1
        elif round == ["B", "Y"]:
            score_p1 += 5
            score_p2 += 5
        elif round == ["B", "Z"]:
            score_p1 += 9
            score_p2 += 9
        elif round == ["C", "X"]:
            score_p1 += 7
            score_p2 += 2
        elif round == ["C", "Y"]:
            score_p1 += 2
            score_p2 += 6
        elif round == ["C", "Z"]:
            score_p1 += 6
            score_p2 += 7
    yield score_p1
    yield score_p2
