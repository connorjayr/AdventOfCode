from typing import Iterator, Optional
from util import *


def execute(registers: dict[str, int], instructions: list[str]):
    pc = 0
    while 0 <= pc < len(instructions):
        name, args = instructions[pc].split(maxsplit=1)
        args = args.split(",")
        if name == "hlf":
            registers[args[0]] //= 2
            pc += 1
        elif name == "tpl":
            registers[args[0]] *= 3
            pc += 1
        elif name == "inc":
            registers[args[0]] += 1
            pc += 1
        elif name == "jmp":
            pc += int(args[0])
        elif name == "jie":
            pc += int(args[1]) if registers[args[0]] % 2 == 0 else 1
        elif name == "jio":
            pc += int(args[1]) if registers[args[0]] == 1 else 1


def solve(input: Optional[str]) -> Iterator[any]:
    instructions = input.split("\n")

    registers = {"a": 0, "b": 0}
    execute(registers, instructions)
    yield registers["b"]

    registers = {"a": 1, "b": 0}
    execute(registers, instructions)
    yield registers["b"]
