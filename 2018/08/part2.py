import sys

class Header:
  def __init__(self, license: list):
    children = license.pop(0)
    entries = license.pop(0)
    
    self.children = []
    for i in range(children):
      self.children.append(Header(license))

    self.entries = []
    for i in range(entries):
      self.entries.append(license.pop(0))

  def get_value(self):
    if len(self.children) == 0: return sum(self.entries)

    value = 0
    for entry in self.entries:
      if 0 < entry <= len(self.children):
        value += self.children[entry - 1].get_value()
    return value

with open(sys.argv[1], "r") as input_file:
  root = Header([int(n) for n in input_file.read().strip().split()])

print(root.get_value())