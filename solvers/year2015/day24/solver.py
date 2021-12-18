from functools import reduce
from itertools import combinations
import operator
from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    packages = set(int(package) for package in input.split("\n"))

    ideal = math.inf
    for first_group_size in range(1, len(packages) - 1):
        print(first_group_size)
        if ideal != math.inf:
            break
        for second_group_size in range(1, len(packages) - first_group_size):
            print(second_group_size)
            for first_group in combinations(packages, first_group_size):
                remaining = packages.difference(set(first_group))
                for second_group in combinations(packages, second_group_size):
                    third_group = remaining.difference(set(second_group))
                    if sum(first_group) == sum(second_group) == sum(third_group):
                        ideal = min(ideal, reduce(operator.mul, first_group, 1))
    yield ideal
