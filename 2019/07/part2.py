import itertools
import sys

class Computer:
  def __init__(self, intcode):
    self.intcode = list(intcode)
    self.pc = 0
    self.halted = False
    
    self.in_values = []
    self.out_values = []

  def get_param(self, mode: str, value: int) -> int:
    if mode == "0":
      return self.intcode[value]
    elif mode == "1":
      return value
    return None

  def exec_until_pause(self):
    if self.halted:
      return
    while self.pc < len(self.intcode):
      inst = str(self.intcode[self.pc]).zfill(5)
      opcode = int(inst[-2:])
      if opcode == 1:
        self.intcode[self.intcode[self.pc + 3]] = self.get_param(inst[2], self.intcode[self.pc + 1]) + self.get_param(inst[1], self.intcode[self.pc + 2])
        self.pc += 4
      elif opcode == 2:
        self.intcode[self.intcode[self.pc + 3]] = self.get_param(inst[2], self.intcode[self.pc + 1]) * self.get_param(inst[1], self.intcode[self.pc + 2])
        self.pc += 4
      elif opcode == 3:
        if len(self.in_values) == 0:
          return
        self.intcode[self.intcode[self.pc + 1]] = self.in_values.pop(0)
        self.pc += 2
      elif opcode == 4:
        self.out_values.append(self.get_param(inst[2], self.intcode[self.pc + 1]))
        self.pc += 2
      elif opcode == 5:
        if self.get_param(inst[2], self.intcode[self.pc + 1]):
          self.pc = self.get_param(inst[1], self.intcode[self.pc + 2])
        else:
          self.pc += 3
      elif opcode == 6:
        if not self.get_param(inst[2], self.intcode[self.pc + 1]):
          self.pc = self.get_param(inst[1], self.intcode[self.pc + 2])
        else:
          self.pc += 3
      elif opcode == 7:
        self.intcode[self.intcode[self.pc + 3]] = int(self.get_param(inst[2], self.intcode[self.pc + 1]) < self.get_param(inst[1], self.intcode[self.pc + 2]))
        self.pc += 4
      elif opcode == 8:
        self.intcode[self.intcode[self.pc + 3]] = int(self.get_param(inst[2], self.intcode[self.pc + 1]) == self.get_param(inst[1], self.intcode[self.pc + 2]))
        self.pc += 4
      elif opcode == 99:
        self.halted = True
        return

with open(sys.argv[1], "r") as input_file:
  software = [int(n) for n in input_file.read().split(",")]

permutations = itertools.permutations(range(5, 10))
max_signal = 0
for settings in permutations:
  amplifiers = [Computer(software) for _ in range(5)]
  for i in range(5):
    amplifiers[i].in_values.append(settings[i])

  in_signal = 0
  i = 0
  while not amplifiers[-1].halted:
    amplifiers[i].in_values.append(in_signal)
    amplifiers[i].exec_until_pause()
    in_signal = amplifiers[i].out_values[-1]
    i = (i + 1) % len(amplifiers)
  max_signal = max(max_signal, amplifiers[-1].out_values[-1])
print(max_signal)
