import math
import sys

def expand_bbox(bbox: list, coordinate: list):
  if len(bbox) == 0:
    bbox.append(list(coordinate))
    bbox.append(list(coordinate))
    return
  bbox[0][0] = min(bbox[0][0], coordinate[0])
  bbox[0][1] = min(bbox[0][1], coordinate[1])
  bbox[1][0] = max(bbox[1][0], coordinate[0])
  bbox[1][1] = max(bbox[1][1], coordinate[1])

def get_manhattan_dist(a: list, b: list) -> int:
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

coordinates = []
bbox = []
with open(sys.argv[1], "r") as input_file:
  for line in input_file.readlines():
    coordinate = [int(n) for n in line.split(",")]
    coordinate.reverse()

    coordinates.append(coordinate)
    expand_bbox(bbox, coordinate)

bbox[0][0] -= 1
bbox[0][1] -= 1
bbox[1][0] += 1
bbox[1][1] += 1

width = bbox[1][1] - bbox[0][1] + 1
height = bbox[1][0] - bbox[0][0] + 1
grid = [[-1 for j in range(width)] for i in range(height)]

areas = {}
infinite_areas = set()
for row in range(height):
  for col in range(width):
    coordinate = [row, col]

    closest = -1
    min_dist = math.inf
    for i in range(len(coordinates)):
      dist = get_manhattan_dist(coordinate, coordinates[i])
      if dist < min_dist:
        closest = i
        min_dist = dist
      elif dist == min_dist:
        closest = -1

    grid[row][col] = closest
    areas[closest] = areas.get(closest, 0) + 1
    if row == 0 or row + 1 == len(grid) or col == 0 or col + 1 == len(grid[row]):
      infinite_areas.add(closest)

max_area = 0
for i, area in areas.items():
  if i in infinite_areas: continue
  max_area = max(max_area, area)

print(max_area)