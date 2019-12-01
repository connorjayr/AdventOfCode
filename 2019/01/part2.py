import sys

def get_fuel(n: int) -> int:
  fuel = n // 3 - 2
  return fuel + get_fuel(fuel) if fuel > 0 else 0

requirements = []
with open(sys.argv[1], "r") as input_file:
  requirements = [int(n) for n in input_file.readlines()]

print(sum([get_fuel(n) for n in requirements]))