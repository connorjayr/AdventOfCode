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

# the border expansion was found through trial and error (for when the area below
# stopped increasing)...there is definitely a better way to do this
bbox[0][0] -= 50
bbox[0][1] -= 50
bbox[1][0] += 50
bbox[1][1] += 50

width = bbox[1][1] - bbox[0][1] + 1
height = bbox[1][0] - bbox[0][0] + 1
grid = [[-1 for j in range(width)] for i in range(height)]

area = 0
for row in range(height):
  for col in range(width):
    coordinate = [row, col]

    dist_sum = 0
    for i in range(len(coordinates)):
      dist_sum += get_manhattan_dist(coordinate, coordinates[i])

    if dist_sum < 10000:
      area += 1

print(area)