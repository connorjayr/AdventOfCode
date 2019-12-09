import sys

def calc_fuel(n: int) -> int:
  fuel = n // 3 - 2
  return fuel + calc_fuel(fuel) if fuel > 0 else 0

with open(sys.argv[1], "r") as input_file:
  masses = [int(mass) for mass in input_file]

# PART 1
print(sum([n // 3 - 2 for n in masses]))
# PART 2
print(sum([calc_fuel(mass) for mass in masses]))