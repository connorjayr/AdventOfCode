from typing import Counter, Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    messages = input.split("\n")
    yield "".join(
        Counter[str](msg[idx] for msg in messages).most_common(1)[0][0]
        for idx in range(len(messages[0]))
    )
    yield "".join(
        Counter[str](msg[idx] for msg in messages).most_common()[-1][0]
        for idx in range(len(messages[0]))
    )
