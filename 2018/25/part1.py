from queue import Queue
import sys

def get_manhattan_dist(p, q):
  return abs(p[0] - q[0]) + abs(p[1] - q[1]) + abs(p[2] - q[2]) + abs(p[3] - q[3])

points = []
with open(sys.argv[1], "r") as input_file:
  for line in input_file.readlines():
    coords = [int(coord) for coord in line.strip().split(",")]
    points.append((coords[0], coords[1], coords[2], coords[3]))

graph = {}
for p in points:
  graph[p] = []
  for q in points:
    if p == q: continue

    if get_manhattan_dist(p, q) <= 3:
      graph[p].append(q)

constellations = 0

visited = set()
for p in points:
  if p in visited: continue

  queue = Queue()
  queue.put(p)
  while not queue.empty():
    q = queue.get()
    visited.add(q)
    for neighbor in graph[q]:
      if neighbor in visited: continue
      queue.put(neighbor)

  constellations += 1

print(constellations)
