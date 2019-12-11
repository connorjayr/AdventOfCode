from ..common.intcode import Computer
import sys

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def move(computer: Computer, grid: dict, d: int, point: tuple) -> tuple:
  computer.in_values.append(grid.get(point, 0))
  computer.exec_until_pause()
  grid[point] = computer.out_values[-2]
  
  d = (d + (1 if computer.out_values[-1] == 1 else -1)) % len(directions)
  point = (point[0] + directions[d][0], point[1] + directions[d][1])
  return d, point


def print_grid(grid: dict):
  points = grid.keys()
  min_point = (min([point[0] for point in points]), min([point[1] for point in points]))
  max_point = (max([point[0] for point in points]), max([point[1] for point in points]))

  for y in range(min_point[1], max_point[1] + 1):
    for x in range(min_point[0], max_point[0] + 1):
      print("█" if grid.get((x, y)) == 1 else " ", end="")
    print()

with open(sys.argv[1], "r") as input_file:
  intcode = [int(value) for value in input_file.read().split(",")]

# PART 1
grid = {(0, 0): 0}
point = (0, 0)
d = 0
computer = Computer(intcode)
while not computer.halted:
  d, point = move(computer, grid, d, point)
print(len(grid))

# PART 2
grid = {(0, 0): 1}
point = (0, 0)
d = 0
computer = Computer(intcode)
while not computer.halted:
  d, point = move(computer, grid, d, point)
print_grid(grid)