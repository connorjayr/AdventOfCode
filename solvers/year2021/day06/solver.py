from typing import Counter, Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    initial_timers = [int(timer) for timer in input.split(",")]
    fish = Counter[int](initial_timers)

    day = 0
    while day < 256:
        num = fish[day]
        fish[day + 7] += num
        fish[day + 9] += num
        day += 1
        if day == 80 or day == 256:
            yield sum(num for future_day, num in fish.items() if future_day >= day)
