from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Iterator, Optional
from util import *


class State:
    registers: defaultdict[str, int]
    last_played: int = 0

    def __init__(self) -> "State":
        self.registers = defaultdict(int)

    def get_value(self, val_or_register: str) -> int:
        try:
            return int(val_or_register)
        except ValueError:
            return self.registers.get(val_or_register, 0)


class Program:
    instructions: list[str]
    pc: int = 0
    state: State

    first_recovered: Optional[int] = None

    dest: "Optional[Program]" = None
    queue: deque[int]
    num_sent: int = 0

    def __init__(self, instructions: list[str]) -> "Program":
        self.instructions = instructions
        self.state = State()
        self.queue = deque()

    def step(self) -> bool:
        if self.pc < 0 or self.pc >= len(self.instructions):
            return False
        name, *args = self.instructions[self.pc].split()
        if name == "snd":
            if self.dest is None:
                self.state.last_played = self.state.get_value(args[0])
            else:
                self.dest.queue.append(self.state.get_value(args[0]))
                self.num_sent += 1
        elif name == "set":
            self.state.registers[args[0]] = self.state.get_value(args[1])
        elif name == "add":
            self.state.registers[args[0]] += self.state.get_value(args[1])
        elif name == "mul":
            self.state.registers[args[0]] *= self.state.get_value(args[1])
        elif name == "mod":
            self.state.registers[args[0]] %= self.state.get_value(args[1])
        elif name == "rcv":
            if self.dest is None:
                if self.state.get_value(args[0]) != 0:
                    self.state.registers[args[0]] = self.state.last_played
                    if self.first_recovered is None:
                        self.first_recovered = self.state.last_played
            else:
                if len(self.queue) == 0:
                    return False
                self.state.registers[args[0]] = self.queue.popleft()
        elif name == "jgz":
            if self.state.get_value(args[0]) > 0:
                self.pc += self.state.get_value(args[1])
                return True
        self.pc += 1
        return True


def solve(input: Optional[str]) -> Iterator[any]:
    instructions = input.split("\n")

    program = Program(instructions)
    while program.first_recovered is None:
        program.step()
    yield program.first_recovered

    programs = [Program(instructions), Program(instructions)]
    for idx in range(len(programs)):
        programs[idx].dest = programs[1 - idx]
        programs[idx].state.registers["p"] = idx

    terminated = False
    while not terminated:
        terminated = True
        for program in programs:
            if program.step():
                terminated = False
    yield programs[1].num_sent
