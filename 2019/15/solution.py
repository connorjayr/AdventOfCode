from ..common.intcode import Computer
import sys

def get_adjacent_points(point: tuple) -> list:
  return [
    (point[0] - 1, point[1]),
    (point[0], point[1] - 1),
    (point[0] + 1, point[1]),
    (point[0], point[1] + 1)
  ]

def get_path(grid: dict, begin: tuple, end: tuple) -> list:
  queue = []
  queue.append([begin])
  while len(queue) > 0:
    path = queue.pop(0)
    point = path[-1]
    if point == end:
      return path
    for adj_point in get_adjacent_points(point):
      if adj_point in path:
        continue
      adj_path = list(path)
      adj_path.append(adj_point)
      if adj_point == end:
        return adj_path
      elif grid.get(adj_point, 0) != 0:
        queue.append(adj_path)
  return None

def get_commands(path: list) -> list:
  commands = []
  for i in range(len(path) - 1):
    begin = path[i]
    end = path[i + 1]
    if begin[0] != end[0]:
      commands.append(4 if begin[0] < end[0] else 3)
    else:
      commands.append(2 if begin[1] < end[1] else 1)
  return commands

def print_grid(grid: dict):
  min_point = (min([point[0] for point in grid]), min([point[1] for point in grid]))
  max_point = (max([point[0] for point in grid]), max([point[1] for point in grid]))
  for y in range(min_point[1], max_point[1] + 1):
    for x in range(min_point[0], max_point[0] + 1):
      status = grid.get((x, y), 3)
      char = "?"
      if status == 0:
        char = "#"
      elif status == 1:
        char = " "
      elif status == 2:
        char = "O"
      print(char, end="")
    print()

with open(sys.argv[1], "r") as input_file:
  intcode = [int(value) for value in input_file.read().split(",")]

computer = Computer(intcode)
point = (0, 0)
grid = {(0, 0): 1}
unknown = [(-1, 0), (0, -1), (1, 0), (0, 1)]
while len(unknown) > 0:
  next_point = unknown.pop()

  path = get_path(grid, point, next_point)
  computer.in_values.extend(get_commands(path))
  computer.exec_until_pause()

  status = computer.out_values[-1]
  if status == 0:
    point = path[-2]
    grid[path[-1]] = 0
  else:
    point = path[-1]
    grid[point] = status
    unknown.extend([point for point in get_adjacent_points(point) if point not in grid and point not in unknown])

oxygen = [point for point, status in grid.items() if status == 2][0]

# PART 1
print(len(get_path(grid, oxygen, (0, 0))) - 1)
# PART 2
print(max([len(get_path(grid, oxygen, point)) - 1 for point in grid if grid[point] != 0]))