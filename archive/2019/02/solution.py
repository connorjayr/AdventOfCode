from ..common.intcode import Computer
import sys

with open(sys.argv[1], "r") as input_file:
  intcode = [int(value) for value in input_file.read().split(",")]

# PART 1
computer = Computer(intcode)
computer.intcode[1] = 2
computer.intcode[2] = 12

computer.exec_until_pause()
print(computer.intcode[0])

# PART 2
for noun in range(len(intcode)):
  for verb in range(len(intcode)):
    computer = Computer(intcode)
    computer.intcode[1] = noun
    computer.intcode[2] = verb
    
    computer.exec_until_pause()
    if computer.intcode[0] == 19690720:
      print(100 * noun + verb)