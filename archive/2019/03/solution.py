import sys

dx = {"U": 0, "R": 1, "D": 0, "L": -1}
dy = {"U": 1, "R": 0, "D": -1, "L": 0}

def get_manhattan_dist(a: tuple, b: tuple) -> int:
  return sum([abs(a[i] - b[i]) for i in range(len(a))])

def parse_wire(path: str, wire: dict):
  point = (0, 0)
  count = 0
  for step in path.split(","):
    direction = step[0]
    for _ in range(int(step[1:])):
      point = (point[0] + dx[direction], point[1] + dy[direction])
      count += 1
      if point not in wire:
        wire[point] = count

wires = []
with open(sys.argv[1], "r") as input_file:
  for path in input_file:
    wires.append({})
    parse_wire(path, wires[-1])

intersections = set(wires[0].keys()).intersection(set(wires[1].keys()))

# PART 1
print(min([get_manhattan_dist((0, 0), point) for point in intersections]))
# PART 2
print(min([wires[0][point] + wires[1][point] for point in intersections]))