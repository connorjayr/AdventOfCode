import math
import sys

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def tile_at(maze: list, point: tuple) -> str:
  if point[0] < 0 or point[1] < 0 or point[1] >= len(maze) or point[0] >= len(maze[point[1]]):
    return " "
  return maze[point[1]][point[0]]

def get_portal_name(maze: list, point: tuple) -> str:
  if tile_at(maze, point) != ".":
    return None
  for d in directions:
    name = "".join([tile_at(maze, (point[0] + d[0] * i, point[1] + d[1] * i)) for i in range(1, 3)])
    if sum(d) < 0:
      name = name[::-1]
    if name.isalpha():
      return name

def find_portals(maze: list) -> tuple:
  portals_by_name = {}
  for y in range(len(maze)):
    for x in range(len(maze[y])):
      name = get_portal_name(maze, (x, y))
      if name is not None:
        portals_by_name.setdefault(name, [])
        portals_by_name[name].append((x, y))
  portals = {}
  for points in portals_by_name.values():
    if len(points) < 2:
      continue
    portals[points[0]] = points[1]
    portals[points[1]] = points[0]
  return portals, portals_by_name

def get_path_length(maze: list, portals: dict, start: tuple, dest: tuple, has_depth: bool) -> int:
  queue = [start]
  visited = set(queue)
  length = 0
  while dest not in queue:
    queue_len = len(queue)
    for _ in range(queue_len):
      point = queue.pop(0)

      to_points = [(point[0], point[1] + d[0], point[2] + d[1]) for d in directions]
      if (point[1], point[2]) in portals:
        if has_depth:
          outside = point[1] == 2 or point[2] == 2 or point[2] == len(maze) - 3 or point[1] == len(maze[point[2]]) - 3
          if not outside or point[0] > 0:
            to_points.append((point[0] + (-1 if outside else 1),) + portals[(point[1], point[2])])
        else:
          to_points.append((point[0],) + portals[(point[1], point[2])])
      for to_point in to_points:
        if to_point in visited or tile_at(maze, (to_point[1], to_point[2])) != ".":
          continue
        queue.append(to_point)
        visited.add(to_point)
    length += 1
  return length

with open(sys.argv[1], "r") as input_file:
  maze = [line.strip("\n") for line in input_file.readlines()]
portals, portals_by_name = find_portals(maze)

# PART 1
print(get_path_length(maze, portals, (0,) + portals_by_name["AA"][0], (0,) + portals_by_name["ZZ"][0], False))
# PART 2
print(get_path_length(maze, portals, (0,) + portals_by_name["AA"][0], (0,) + portals_by_name["ZZ"][0], True))