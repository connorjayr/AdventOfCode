from typing import Dict, Generator, List, Optional
from util import *


def run_program(program: List[str], registers: Dict[str, int]) -> int:
    """Runs an assembunny program.

    Args:
        program: The list of instructions.
        registers: The registers, which will be modified as the program runs.
    """
    pc = 0
    while pc < len(program):
        name, *args = program[pc].split()
        if name == "cpy":
            source, dest = args
            if source in registers:
                registers[dest] = registers[source]
            else:
                registers[dest] = int(source)
        elif name == "inc":
            registers[args[0]] += 1
        elif name == "dec":
            registers[args[0]] -= 1
        elif name == "jnz":
            source, offset = args
            if (source in registers and registers[source] != 0) or (
                source not in registers and int(source) != 0
            ):
                pc += int(offset)
                continue
        else:
            raise InputError(f'unknown instruction "{name}"')
        pc += 1


def solve(input: Optional[str]) -> Generator[any, None, None]:
    program = input.split("\n")

    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    run_program(program, registers)
    yield registers["a"]

    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    run_program(program, registers)
    yield registers["a"]
