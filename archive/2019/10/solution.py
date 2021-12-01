import math
import sys

def simplify(frac: tuple) -> tuple:
  gcd = math.gcd(frac[0], frac[1])
  return (frac[0] // gcd, frac[1] // gcd)

def count_visible_asteroids(asteroids: list, source: tuple) -> int:
  lines_of_sight = set()
  for point in asteroids:
    if source == point:
      continue
    lines_of_sight.add(simplify((point[0] - source[0], point[1] - source[1])))
  return len(lines_of_sight)

def get_slope(frac: tuple):
  return frac[1] / frac[0] if frac[0] != 0 else math.inf

def get_clockwise_asteroids(asteroids: list, source: tuple) -> list:
  right_set = set()
  left_set = set()
  for point in asteroids:
    if source == point:
      continue
    if point[0] >= source[0]:
      right_set.add(simplify((point[0] - source[0], point[1] - source[1])))
    else:
      left_set.add(simplify((point[0] - source[0], point[1] - source[1])))

  right = list(right_set)
  right.sort(key=lambda point: -1 * get_slope(point))
  left = list(left_set)
  left.sort(key=lambda point: get_slope(point))

  right.extend(left)
  return right

def get_angle_map(asteroids: list, source: tuple) -> dict:
  angle_map = {}
  for point in asteroids:
    if source == point:
      continue
    angle = simplify((point[0] - source[0], point[1] - source[1]))
    angle_map.setdefault(angle, [])
    angle_map[angle].append(point)
  for points in angle_map.values():
    points.sort(key=lambda point: math.hypot(point[0] - source[0], point[1] - source[1]))
  return angle_map

asteroid_map = []
asteroids = []
with open(sys.argv[1], "r") as input_file:
  row = []
  y = 0
  for line in input_file:
    x = 0
    for point in line.strip():
      if point == "#":
        row.append(1)
        asteroids.append((x, y))
      else:
        row.append(0)
      x += 1
    asteroid_map.append(row)
    y += 1

# PART 1
max_point = max(asteroids, key=lambda point: count_visible_asteroids(asteroids, point))
print(count_visible_asteroids(asteroids, max_point))

# PART 2
clockwise = get_clockwise_asteroids(asteroids, max_point)
angle_map = get_angle_map(asteroids, max_point)
i = 0
destroyed = 0
while len(angle_map) > 0:
  angle = clockwise[i]
  if angle in angle_map:
    point = angle_map[angle].pop(0)
    destroyed += 1
    if destroyed == 200:
      print(100 * point[0] + point[1])
    if len(angle_map[angle]) == 0:
      del angle_map[angle]
  i = (i + 1) % len(clockwise)