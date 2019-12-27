from ..common.intcode import Computer
import sys

def add_instruction(computer: Computer, instruction: str):
  computer.in_values.extend([ord(c) for c in instruction] + [ord("\n")])

with open(sys.argv[1], "r") as input_file:
  intcode = [int(value) for value in input_file.read().split(",")]

# PART 1
computer = Computer(intcode)
add_instruction(computer, "NOT A T")
add_instruction(computer, "NOT B J")
add_instruction(computer, "OR T J")
add_instruction(computer, "NOT C T")
add_instruction(computer, "OR T J")
add_instruction(computer, "AND D J")
add_instruction(computer, "WALK")
computer.exec_until_pause()
print(computer.out_values[-1])

# PART 2
computer = Computer(intcode)
add_instruction(computer, "NOT A T")
add_instruction(computer, "NOT B J")
add_instruction(computer, "OR T J")
add_instruction(computer, "NOT C T")
add_instruction(computer, "OR T J")
add_instruction(computer, "AND D J")
add_instruction(computer, "NOT H T")
add_instruction(computer, "NOT T T")
add_instruction(computer, "OR E T")
add_instruction(computer, "AND T J")
add_instruction(computer, "RUN")
computer.exec_until_pause()
print(computer.out_values[-1])