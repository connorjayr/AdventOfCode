import sys

class Node:
  def __init__(self, value):
    self.prev = self
    self.next = self
    self.value = value

  def insert(self, value):
    new_node = Node(value)
    new_node.prev = self.prev
    new_node.next = self
    self.prev.next = new_node
    self.prev = new_node
    return new_node

  def remove(self):
    self.prev.next = self.next
    self.next.prev = self.prev
    return self.next

with open(sys.argv[1], "r") as input_file:
  contents = input_file.read().split()
  elves = int(contents[0])
  last_marble = int(contents[6]) * 100

scores = [0 for i in range(elves)]

elf = 0
current_marble = Node(0)
for marble in range(1, last_marble + 1):
  if marble % 23 != 0:
    current_marble = current_marble.next.next.insert(marble)
  else:
    scores[elf] += marble
    current_marble = current_marble.prev.prev.prev.prev.prev.prev.prev
    scores[elf] += current_marble.value
    current_marble = current_marble.remove()
  elf = (elf + 1) % elves

print(max(scores))