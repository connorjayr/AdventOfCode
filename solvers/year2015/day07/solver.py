from collections import defaultdict
from dataclasses import dataclass
import re
from typing import Iterator, Optional, Union
from util import *


@dataclass
class Instruction:
    operator: Optional[str]
    sources: list[str]
    dest: str


class Circuit:
    wires: dict[str, int]
    instructions: defaultdict[Optional[str], list[Instruction]]

    def __init__(self):
        self.wires = {}
        self.instructions = defaultdict(list[Instruction])

    def add_instruction(self, instruction: Instruction):
        added = False
        for source in instruction.sources:
            if not source.isdigit():
                self.instructions[source].append(instruction)
                added = True
        if not added:
            self.instructions[None].append(instruction)

    def get_signal(self, wire_or_signal: Union[str, int]) -> Optional[int]:
        if wire_or_signal.isdigit():
            return int(wire_or_signal)
        else:
            return self.wires.get(wire_or_signal)

    def execute(self, instruction: Instruction):
        can_execute = True
        for source in instruction.sources:
            if not source.isdigit() and source not in self.wires:
                can_execute = False
                break
        if not can_execute:
            return

        if instruction.operator == None:
            self.wires[instruction.dest] = self.get_signal(instruction.sources[0])
        elif instruction.operator == "NOT":
            self.wires[instruction.dest] = ~self.get_signal(instruction.sources[0])
        elif instruction.operator == "AND":
            self.wires[instruction.dest] = self.get_signal(
                instruction.sources[0]
            ) & self.get_signal(instruction.sources[1])
        elif instruction.operator == "OR":
            self.wires[instruction.dest] = self.get_signal(
                instruction.sources[0]
            ) | self.get_signal(instruction.sources[1])
        elif instruction.operator == "LSHIFT":
            self.wires[instruction.dest] = self.get_signal(
                instruction.sources[0]
            ) << self.get_signal(instruction.sources[1])
        elif instruction.operator == "RSHIFT":
            self.wires[instruction.dest] = self.get_signal(
                instruction.sources[0]
            ) >> self.get_signal(instruction.sources[1])

        for next_instruction in self.instructions.get(instruction.dest, []):
            self.execute(next_instruction)

    def emulate(self):
        for instruction in self.instructions[None]:
            self.execute(instruction)


def solve(input: Optional[str]) -> Iterator[any]:
    circuit = Circuit()
    for instruction in input.split("\n"):
        if match := re.match(r"(\d+|[a-z]+) -> ([a-z]+)", instruction):
            source, dest = match.groups()
            circuit.add_instruction(Instruction(None, [source], dest))
        elif match := re.match(r"NOT (\d+|[a-z]+) -> ([a-z])+", instruction):
            source, dest = match.groups()
            circuit.add_instruction(Instruction("NOT", [source], dest))
        elif match := re.match(
            r"(\d+|[a-z]+) (AND|OR|LSHIFT|RSHIFT) (\d+|[a-z]+) -> ([a-z])+", instruction
        ):
            lhs, operator, rhs, dest = match.groups()
            circuit.add_instruction(Instruction(operator, [lhs, rhs], dest))
    circuit.emulate()
    yield circuit.get_signal("a")
