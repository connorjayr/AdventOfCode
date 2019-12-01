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

  def get_entry_sum(self):
    result = sum(self.entries)
    for child in self.children:
      result += child.get_entry_sum()
    return result

with open(sys.argv[1], "r") as input_file:
  root = Header([int(n) for n in input_file.read().strip().split()])

print(root.get_entry_sum())