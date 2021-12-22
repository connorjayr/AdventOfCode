import re
from typing import Iterator, Optional
from util import *


def get_score(groups: str) -> int:
    score = 0
    depth = 0
    for c in groups:
        if c == "{":
            depth += 1
        elif c == "}":
            score += depth
            depth -= 1
    return score


def solve(input: Optional[str]) -> Iterator[any]:
    after_ignore = re.sub(r"!.", "", input)
    yield get_score(re.sub(r"<[^>]*>", "", after_ignore))
    yield sum(len(garbage) - 2 for garbage in re.findall(r"<[^>]*>", after_ignore))
