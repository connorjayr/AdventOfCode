import math
import sys

def remove_units(polymer: str, unit: str) -> str:
  polymer = polymer.replace(unit.lower(), "")
  polymer = polymer.replace(unit.upper(), "")
  return polymer

def can_react(a: str, b: str) -> bool:
  return a != b and a.lower() == b.lower()

polymer = ""
with open(sys.argv[1], "r") as input_file:
  polymer = input_file.read().strip()

shortest = math.inf
for unit in [chr(c) for c in range(ord("a"), ord("z") + 1)]:
  new_polymer = remove_units(polymer, unit)
  i = 0
  while i + 1 < len(new_polymer):
    if can_react(new_polymer[i], new_polymer[i + 1]):
      new_polymer = new_polymer[:i] + new_polymer[i + 2:]
      i = max(i - 1, 0)
    else:
      i += 1
  shortest = min(shortest, len(new_polymer))


print(shortest)