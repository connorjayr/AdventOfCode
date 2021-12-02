from collections import Counter
from typing import Generator, Optional
from util import *


def solve(input: Optional[str]) -> Generator[any, None, None]:
    messages = input.split("\n")
    yield "".join(
        Counter(msg[idx] for msg in messages).most_common(1)[0][0]
        for idx in range(len(messages[0]))
    )
    yield "".join(
        Counter(msg[idx] for msg in messages).most_common()[-1][0]
        for idx in range(len(messages[0]))
    )
