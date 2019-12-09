from .. import intcode
import sys

with open(sys.argv[1], "r") as input_file:
  computer = intcode.Computer([int(n) for n in input_file.read().split(",")])
computer.in_values.append(2)
computer.exec_until_pause()
print(computer.out_values[0])