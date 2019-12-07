import sys

with open(sys.argv[1], "r") as input_file:
  orig_intcode = [int(n) for n in input_file.read().split(",")]

for noun in range(len(orig_intcode)):
  for verb in range(len(orig_intcode)):
    intcode = list(orig_intcode)

    intcode[1] = noun
    intcode[2] = verb

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

    if intcode[0] == 19690720:
      print(100 * noun + verb)
      exit(0)