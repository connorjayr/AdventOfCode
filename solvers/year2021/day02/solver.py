from typing import Iterator, Optional
from util import *


def solve(input: Optional[str]) -> Iterator[any]:
    dist = 0
    depth = 0
    for line in input.split("\n"):
        command, value = line.split(" ")
        value = int(value)
        if command == "forward":
            dist += value
        elif command == "down":
            depth += value
        elif command == "up":
            depth -= value
        else:
            raise errors.InputError(f'unknown command "{command}"')
    yield dist * depth

    dist = 0
    depth = 0
    aim = 0
    for line in input.split("\n"):
        command, value = line.split(" ")
        value = int(value)
        if command == "forward":
            dist += value
            depth += aim * value
        elif command == "down":
            aim += value
        elif command == "up":
            aim -= value
        else:
            raise InputError(f'unknown command "{command}"')
    yield dist * depth
