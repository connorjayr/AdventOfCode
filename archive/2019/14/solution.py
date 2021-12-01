import math
import sys

def parse_resource(resource: str) -> tuple:
  resource = resource.strip().split()
  return resource[1].strip(), int(resource[0].strip())

def get_required_ore(reactions, fuel_amount):
  required = {"FUEL": fuel_amount}
  while any([required[product] > 0 and product != "ORE" for product in required]):
    product = [product for product in required if required[product] > 0 and product != "ORE"][0]
    
    reaction = reactions[product]
    count = math.ceil(required[product] / reaction[1][1])
    required[product] -= count * reaction[1][1]
    for reactant in reaction[0]:
      required[reactant[0]] = required.get(reactant[0], 0) + count * reactant[1]
  return required["ORE"]

reactions = {}
with open(sys.argv[1], "r") as input_file:
  for line in input_file:
    reaction = line.split("=>")

    reactants = [parse_resource(resource) for resource in reaction[0].split(",")]
    product = parse_resource(reaction[1])
    reactions[product[0]] = (reactants, product)

# PART 1
print(get_required_ore(reactions, 1))

# PART 2
min_fuel = 1
max_fuel = 2
while get_required_ore(reactions, max_fuel) < 1000000000000:
  min_fuel *= 2
  max_fuel *= 2
while min_fuel + 1 < max_fuel:
  mid = (min_fuel + max_fuel) // 2
  mid_ore = get_required_ore(reactions, mid)
  if mid_ore > 1000000000000:
    max_fuel = mid
  elif mid_ore < 1000000000000:
    min_fuel = mid
print(min_fuel)