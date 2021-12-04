import re
from typing import Generator, Optional
from util import *


def decompress_v1(s: str) -> int:
    idx = 0
    while idx < len(s):
        if match := re.match(r"\((\d+)x(\d+)\)", s[idx:]):
            chars, repeat = (int(n) for n in match.groups())
            s = (
                s[:idx]
                + s[idx + match.end() : idx + match.end() + chars] * repeat
                + s[idx + match.end() + chars :]
            )
            idx += chars * repeat
        else:
            idx += 1
    return len(s)


def decompress_v2(s: str) -> int:
    idx = 0
    length = 0
    while idx < len(s):
        if match := re.match(r"\((\d+)x(\d+)\)", s[idx:]):
            chars, repeat = (int(n) for n in match.groups())
            length += (
                decompress_v2(s[idx + match.end() : idx + match.end() + chars]) * repeat
            )
            idx += match.end() + chars
        else:
            idx += 1
            length += 1
    return length


def solve(input: Optional[str]) -> Generator[any, None, None]:
    yield decompress_v1(input)
    yield decompress_v2(input)
