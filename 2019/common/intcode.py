class Computer:
  def __init__(self, intcode):
    self.intcode = {}
    i = 0
    for value in intcode:
      self.intcode[i] = value
      i += 1

    self.pc = 0
    self.relative_base = 0
    
    self.in_values = []
    self.out_values = []

  def get_index(self, param: int) -> int:
    mode = str(self.intcode[self.pc]).zfill(5)[3 - param]
    index = self.intcode.get(self.pc + param, 0)
    if mode == "0":
      return index
    elif mode == "2":
      return self.relative_base + index
    return None

  def get_param(self, param: int) -> int:
    mode = str(self.intcode[self.pc]).zfill(5)[3 - param]
    value = self.intcode.get(self.pc + param, 0)
    if mode == "0":
      return self.intcode.get(value, 0)
    elif mode == "1":
      return value
    elif mode == "2":
      return self.intcode.get(self.relative_base + value, 0)
    return None

  def exec_until_pause(self):
    while self.pc < len(self.intcode):
      inst = str(self.intcode[self.pc]).zfill(5)
      opcode = int(inst[-2:])

      if opcode == 1:
        self.intcode[self.get_index(3)] = self.get_param(1) + self.get_param(2)
        self.pc += 4
      elif opcode == 2:
        self.intcode[self.get_index(3)] = self.get_param(1) * self.get_param(2)
        self.pc += 4
      elif opcode == 3:
        if len(self.in_values) == 0:
          return
        self.intcode[self.get_index(1)] = self.in_values.pop(0)
        self.pc += 2
      elif opcode == 4:
        self.out_values.append(self.get_param(1))
        self.pc += 2
      elif opcode == 5:
        if self.get_param(1):
          self.pc = self.get_param(2)
        else:
          self.pc += 3
      elif opcode == 6:
        if not self.get_param(1):
          self.pc = self.get_param(2)
        else:
          self.pc += 3
      elif opcode == 7:
        self.intcode[self.get_index(3)] = int(self.get_param(1) < self.get_param(2))
        self.pc += 4
      elif opcode == 8:
        self.intcode[self.get_index(3)] = int(self.get_param(1) == self.get_param(2))
        self.pc += 4
      elif opcode == 9:
        self.relative_base += self.get_param(1)
        self.pc += 2
      elif opcode == 99:
        break