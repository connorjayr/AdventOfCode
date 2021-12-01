import sys

class Point:
  def __init__(self, pos: tuple, vel: tuple):
    self.pos = pos
    self.vel = vel

  def move(self, time: int):
    self.pos = (self.pos[0] + self.vel[0] * time, self.pos[1] + self.vel[1] * time)

def get_bbox(points: list) -> tuple:
  top_left = points[0].pos
  bottom_right = points[0].pos
  for point in points:
    top_left = (min(top_left[0], point.pos[0]), min(top_left[1], point.pos[1]))
    bottom_right = (max(bottom_right[0], point.pos[0]), max(bottom_right[1], point.pos[1]))
  return (top_left, bottom_right)

def get_area(bbox: tuple) -> tuple:
  return (bbox[1][0] - bbox[0][0] + 1, bbox[1][1] - bbox[0][1] + 1)

points = []
with open(sys.argv[1], "r") as input_file:
  for line in input_file.readlines():
    pos_end = line.find(">")
    pos = tuple([int(n) for n in line[line.find("<") + 1:pos_end].split(",")])
    vel = tuple([int(n) for n in line[line.find("<", pos_end + 1) + 1:line.find(">", pos_end + 1)].split(",")])
    points.append(Point(pos, vel))

cmd = ""
total_time = 0
while not cmd == "q":
  print("m <time>: move points forward by an amount of time")
  print("p: print the sky")
  print("q: quit")
  cmd = input().strip()

  if cmd.startswith("m"):
    time = int(cmd[2:])
    total_time += time
    for point in points:
      point.move(time)
    bbox = get_bbox(points)
    print("total time:", total_time)
    print("bounding box:", bbox)
    print("area:", get_area(bbox))
  elif cmd == "p":
    bbox = get_bbox(points)
    area = get_area(bbox)
    grid = [[" " for j in range(area[0])] for i in range(area[1])]
    for point in points:
      grid[point.pos[1] - bbox[0][1]][point.pos[0] - bbox[0][0]] = "#"
    
    print()
    for row in grid:
      print("  " + "".join(row))
    print()