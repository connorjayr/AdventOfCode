import sys

def can_react(a: str, b: str) -> bool:
  return a != b and a.lower() == b.lower()

polymer = ""
with open(sys.argv[1], "r") as input_file:
  polymer = input_file.read().strip()

i = 0
while i + 1 < len(polymer):
  if can_react(polymer[i], polymer[i + 1]):
    polymer = polymer[:i] + polymer[i + 2:]
    i = max(i - 1, 0)
  else:
    i += 1

print(len(polymer))