from typing import Generator, Optional
from util.errors import InputError


def solve(input: Optional[str]) -> Generator[any, None, None]:
    distance = 0
    depth = 0
    for line in input.split("\n"):
        command, value = line.split()
        value = int(value)
        if command == "forward":
            distance += value
        elif command == "down":
            depth += value
        elif command == "up":
            depth -= value
        else:
            raise InputError(f'unknown command "{command}"')
    yield distance * depth

    distance = 0
    depth = 0
    aim = 0
    for line in input.split("\n"):
        command, value = line.split()
        value = int(value)
        if command == "forward":
            distance += value
            depth += aim * value
        elif command == "down":
            aim += value
        elif command == "up":
            aim -= value
        else:
            raise InputError(f'unknown command "{command}"')
    yield distance * depth
