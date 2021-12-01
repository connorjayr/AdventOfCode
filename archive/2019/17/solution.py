from ..common.intcode import Computer
import re
import sys

def get_nearby_points(point: tuple) -> list:
  return [
    point,
    (point[0] - 1, point[1]),
    (point[0], point[1] - 1),
    (point[0] + 1, point[1]),
    (point[0], point[1] + 1)
  ]

def has_point(view: list, point: tuple) -> bool:
  return point[0] >= 0 and point[1] >= 0 and point[1] < len(view) and point[0] < len(view[point[1]])

def has_intersection(view: list, point: tuple) -> bool:
  for nearby in get_nearby_points(point):
    if not has_point(view, nearby) or view[nearby[1]][nearby[0]] != "#":
      return False
  return True

with open(sys.argv[1], "r") as input_file:
  intcode = [int(value) for value in input_file.read().split(",")]

# PART 1
computer = Computer(intcode)
computer.exec_until_pause()

view = "".join([chr(value) for value in computer.out_values]).split("\n")
result = 0
for y in range(len(view)):
  for x in range(len(view[y])):
    if has_intersection(view, (x, y)):
      result += x * y
print(result)

# PART 2
def move(point: tuple, d: tuple) -> tuple:
  return (point[0] + d[0], point[1] + d[1])

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
point = (0, 0)
d = 0
for y in range(len(view)):
  for x in range(len(view[y])):
    if view[y][x] == "^":
      point = (x, y)

path = ""
steps = 0
while True:
  point_left = move(point, directions[d - 1])
  point_forward = move(point, directions[d])
  point_right = move(point, directions[(d + 1) % len(directions)])
  if (
    (not has_point(view, point_left) or view[point_left[1]][point_left[0]] != "#")
    and (not has_point(view, point_forward) or view[point_forward[1]][point_forward[0]] != "#")
    and (not has_point(view, point_right) or view[point_right[1]][point_right[0]] != "#")
  ):
    if steps > 0:
      path += str(steps) + ","
    break

  if has_point(view, point_forward) and view[point_forward[1]][point_forward[0]] == "#":
    steps += 1
    point = move(point, directions[d])
  else:
    if steps > 0:
      path += str(steps) + ","
      steps = 0
    if has_point(view, point_left) and view[point_left[1]][point_left[0]] == "#":
      path += "L,"
      d = (d - 1) % len(directions)
    elif has_point(view, point_right) and view[point_right[1]][point_right[0]] == "#":
      path += "R,"
      d = (d + 1) % len(directions)

# print(path)

# A,B,A,C,B,C,A,B,A,C
# A = R,6,L,10,R,8,R,8
# B = R,12,L,8,L,10
# C = R,12,L,10,R,6,L,10

computer = Computer(intcode)
computer.intcode[0] = 2
computer.in_values.extend([ord(c) for c in "A,B,A,C,B,C,A,B,A,C\nR,6,L,10,R,8,R,8\nR,12,L,8,L,10\nR,12,L,10,R,6,L,10\nn\n"])
computer.exec_until_pause()
print(computer.out_values[-1])