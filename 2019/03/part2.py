import sys

dx = {"U": 0, "R": 1, "D": 0, "L": -1}
dy = {"U": 1, "R": 0, "D": -1, "L": 0}

def get_manhattan_dist(a: tuple, b: tuple) -> int:
  return sum([abs(a[i] - b[i]) for i in range(len(a))])

with open(sys.argv[1], "r") as input_file:
  paths = [path.split(",") for path in input_file.readlines()]

wires = []
for path in paths:
  wire = {}
  loc = (0, 0)
  total_steps = 0
  for direction in path:
    steps = int(direction[1:])
    for step in range(steps):
      loc = (loc[0] + dx[direction[0]], loc[1] + dy[direction[0]])
      total_steps += 1
      if loc not in wire:
        wire[loc] = total_steps
  wires.append(wire)

intersections = set(wires[0].keys()).intersection(set(wires[1].keys()))
print(min([wires[0][loc] + wires[1][loc] for loc in intersections]))