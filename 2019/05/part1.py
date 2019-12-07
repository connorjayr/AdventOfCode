import sys

def get_param(intcode: list, mode: str, value: int):
  if mode == "0":
    return intcode[value]
  elif mode == "1":
    return value
  return None

with open(sys.argv[1], "r") as input_file:
  intcode = [int(n) for n in input_file.read().split(",")]

pc = 0
while pc < len(intcode):
  inst = str(intcode[pc]).zfill(5)
  opcode = int(inst[-2:])
  if opcode == 1:
    intcode[intcode[pc + 3]] = get_param(intcode, inst[2], intcode[pc + 1]) + get_param(intcode, inst[1], intcode[pc + 2])
    pc += 4
  elif opcode == 2:
    intcode[intcode[pc + 3]] = get_param(intcode, inst[2], intcode[pc + 1]) * get_param(intcode, inst[1], intcode[pc + 2])
    pc += 4
  elif opcode == 3:
    value = int(input("> "))
    intcode[intcode[pc + 1]] = value
    pc += 2
  elif opcode == 4:
    print(get_param(intcode, inst[2], intcode[pc + 1]))
    pc += 2
  elif opcode == 99:
    break