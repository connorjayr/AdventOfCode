import sys

with open(sys.argv[1], "r") as input_file:
  intcode = [int(n) for n in input_file.read().split(",")]

intcode[1] = 12
intcode[2] = 2

pc = 0
while pc < len(intcode):
  opcode = intcode[pc]
  if opcode == 1:
    intcode[intcode[pc + 3]] = intcode[intcode[pc + 1]] + intcode[intcode[pc + 2]]
    pc += 4
  elif opcode == 2:
    intcode[intcode[pc + 3]] = intcode[intcode[pc + 1]] * intcode[intcode[pc + 2]]
    pc += 4
  elif opcode == 99:
    break

print(intcode[0])