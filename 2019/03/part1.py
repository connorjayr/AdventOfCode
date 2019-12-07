import sys

dx = {"U": 0, "R": 1, "D": 0, "L": -1}
dy = {"U": 1, "R": 0, "D": -1, "L": 0}

def get_manhattan_dist(a: tuple, b: tuple) -> int:
  return sum([abs(a[i] - b[i]) for i in range(len(a))])

with open(sys.argv[1], "r") as input_file:
  paths = [path.split(",") for path in input_file.readlines()]

wires = []
for path in paths:
  wire = set()
  loc = (0, 0)
  for direction in path:
    steps = int(direction[1:])
    for step in range(steps):
      loc = (loc[0] + dx[direction[0]], loc[1] + dy[direction[0]])
      wire.add(loc)
  wires.append(wire)

intersections = wires[0].intersection(wires[1])
print(min([get_manhattan_dist((0, 0), loc) for loc in intersections]))