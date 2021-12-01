from typing import Generator, Optional


def solve(input: Optional[str]) -> Generator[any, None, None]:
    depths = [int(n) for n in input.split()]
    yield sum(depths[i + 1] > depths[i] for i in range(len(depths) - 1))
    yield sum(depths[i + 3] > depths[i] for i in range(len(depths) - 3))
