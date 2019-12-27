from collections import deque
import sys

def adjacent_to(point: tuple) -> list:
  return [
    (point[0] - 1, point[1]),
    (point[0], point[1] - 1),
    (point[0] + 1, point[1]),
    (point[0], point[1] + 1),
  ]

def has_point(vault: list, point: tuple) -> bool:
  return point[0] >= 0 and point[1] >= 0 and point[1] < len(vault) and point[0] < len(vault[point[1]])

def tile_at(vault: list, point: tuple) -> str:
  return vault[point[1]][point[0]] if has_point(vault, point) else "#"

with open(sys.argv[1], "r") as input_file:
  vault = [row.strip("\n") for row in input_file]

entrance = None
for y in range(len(vault)):
  if "@" in vault[y]:
    entrance = (vault[y].index("@"), y)

all_keys = set()
for y in range(len(vault)):
  for x in range(len(vault[y])):
    if vault[y][x].islower():
      all_keys.add(vault[y][x])
key_count = len(all_keys)

queue = deque([(entrance, 0, set())])
visited = set([(entrance, frozenset())])
while len(queue) > 0:
  entry = queue.popleft()
  point = entry[0]
  keys = entry[2]
  if len(keys) == key_count:
    print(entry[1])
    break

  for adj_point in adjacent_to(point):
    adj_tile = tile_at(vault, adj_point)

    adj_keys = set(keys)
    if adj_tile.islower():
      adj_keys.add(adj_tile)

    if (adj_point, frozenset(adj_keys)) in visited or adj_tile == "#" or (adj_tile.isupper() and adj_tile.lower() not in keys and adj_tile.lower() in all_keys):
        continue

    queue.append((adj_point, entry[1] + 1, adj_keys))
    visited.add((adj_point, frozenset(adj_keys)))

# NOTE: The above code is the solutions for PART 1 and PART 2. For PART 2, split
# each quadrant up into four separate input files, and the solution is the sum of
# the outputs for each file.