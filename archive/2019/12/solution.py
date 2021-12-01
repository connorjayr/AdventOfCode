import math
import sys

def lcm(values: list):
  if len(values) == 1:
    return values[0]
  mid = len(values) // 2
  left_lcm = lcm(values[:mid])
  right_lcm = lcm(values[mid:])
  return left_lcm * right_lcm // math.gcd(left_lcm, right_lcm)

class Moon:
  def __init__(self, position, velocity):
    self.position = position
    self.velocity = velocity

  def get_potential_energy(self):
    return sum([abs(n) for n in self.position])

  def get_kinetic_energy(self):
    return sum([abs(n) for n in self.velocity])

  def get_total_energy(self):
    return self.get_potential_energy() * self.get_kinetic_energy()

  def simulate(self, state: list):
    velocity = list(self.velocity)
    for moon in state:
      for dim in range(3):
        if self.position[dim] < moon.position[dim]:
          velocity[dim] += 1
        elif self.position[dim] > moon.position[dim]:
          velocity[dim] -= 1

    position = list(self.position)
    for i in range(3):
      position[i] += velocity[i]

    return Moon(position, velocity)

def parse_moon(line: str):
  prev = 0
  position = []
  for _ in range(3):
    begin = line.find("=", prev)
    end = line.find(",", prev)
    if end == -1:
      end = line.find(">", prev)
    position.append(int(line[begin + 1:end]))
    prev = end + 1
  return Moon(tuple(position), (0, 0, 0))

def get_state_identifier(state: list, dim: int):
  identifier = []
  for moon in state:
    identifier.append(moon.position[dim])
    identifier.append(moon.velocity[dim])
  return tuple(identifier)

begin_state = []
with open(sys.argv[1], "r") as input_file:
  for line in input_file:
    begin_state.append(parse_moon(line))
begin_state_ids = [get_state_identifier(begin_state, dim) for dim in range(3)]

state = list(begin_state)
for i in range(1000):
  next_state = []
  for moon in state:
    next_state.append(moon.simulate(state))
  state = next_state
print(sum([moon.get_total_energy() for moon in state]))

state = list(begin_state)
steps = 0
period = [0, 0, 0]
while 0 in period:
  for dim in range(3):
    if period[dim] != 0:
      continue
    if get_state_identifier(state, dim) == begin_state_ids[dim]:
      period[dim] = steps

  next_state = []
  for moon in state:
    next_state.append(moon.simulate(state))
  state = next_state

  steps += 1

print(lcm(period))