from ..common.intcode import Computer
import sys

with open(sys.argv[1], "r") as input_file:
  intcode = [int(value) for value in input_file.read().split(",")]

# PART 1
computer = Computer(intcode)
computer.in_values.append(1)
computer.exec_until_pause()
print(computer.out_values[-1])

# PART 2
computer = Computer(intcode)
computer.in_values.append(5)
computer.exec_until_pause()
print(computer.out_values[-1])