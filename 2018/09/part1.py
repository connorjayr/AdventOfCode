import sys

with open(sys.argv[1], "r") as input_file:
  contents = input_file.read().split()
  elves = int(contents[0])
  last_marble = int(contents[6])

scores = [0 for i in range(elves)]

elf = 0
circle = [0]
current_marble = 0
for marble in range(1, last_marble + 1):
  if marble % 23 != 0:
    current_marble = (current_marble + 2) % len(circle)
    circle.insert(current_marble, marble)
  else:
    scores[elf] += marble
    current_marble = (current_marble - 7 + len(circle)) % len(circle)
    scores[elf] += circle.pop(current_marble)
    current_marble %= len(circle)
  elf = (elf + 1) % elves

print(max(scores))