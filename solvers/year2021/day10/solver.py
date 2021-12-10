from collections import deque
from typing import Iterator, Optional, TextIO, Union
from util import *


MATCHING_BRACKETS = {"(": ")", "[": "]", "<": ">", "{": "}"}


def test(line: str) -> Union[int, list[str]]:
    """Tests a line that is either incomplete or corrupted.

    Args:
        line: The line to test.

    Returns:
        Either a score representing the first invalid closing bracket in the
        line, or a queue representing the unclosed opening brackets at the end
        of testing.
    """
    queue = []
    for bracket in line:
        if bracket in MATCHING_BRACKETS:
            queue.append(bracket)
        else:
            closing_bracket = MATCHING_BRACKETS[queue.pop()]
            if closing_bracket != bracket:
                return {")": 3, "]": 57, "}": 1197, ">": 25137}.get(bracket)
    return queue


def solve(input: Optional[str]) -> Iterator[any]:
    lines = input.split("\n")

    total_score = 0
    incomplete_queues = []
    for line in lines:
        result = test(line)
        if type(result) == int:
            total_score += result
        else:
            incomplete_queues.append(result)
    yield total_score

    scores = []
    for queue in incomplete_queues:
        score = 0
        while len(queue) > 0:
            opening_bracket = queue.pop()
            score *= 5
            score += {"(": 1, "[": 2, "{": 3, "<": 4}.get(opening_bracket)
        scores.append(score)
    scores.sort()
    yield scores[len(scores) // 2]
