import sys

WIDTH = 5
HEIGHT = 5

def print_layout(layout: list):
  for y in range(HEIGHT):
    for x in range(WIDTH):
      print("#" if (x, y) in layout else ".", end="")
    print()
  print()

def deep_adjacent_to(space: tuple) -> list:
  depth = space[0]
  
  adj_spaces = adjacent_to((space[1], space[2]))
  deep_adj_spaces = []
  for adj in adj_spaces:
    if adj[0] < 0:
      deep_adj_spaces.append((depth - 1, 1, 2))
    elif adj[0] >= WIDTH:
      deep_adj_spaces.append((depth - 1, 3, 2))
    elif adj[1] < 0:
      deep_adj_spaces.append((depth - 1, 2, 1))
    elif adj[1] >= HEIGHT:
      deep_adj_spaces.append((depth - 1, 2, 3))
    elif adj == (2, 2):
      if space[1] == 1:
        deep_adj_spaces.extend([(depth + 1, 0, y) for y in range(HEIGHT)])
      elif space[1] == 3:
        deep_adj_spaces.extend([(depth + 1, WIDTH - 1, y) for y in range(HEIGHT)])
      elif space[2] == 1:
        deep_adj_spaces.extend([(depth + 1, x, 0) for x in range(WIDTH)])
      elif space[2] == 3:
        deep_adj_spaces.extend([(depth + 1, x, HEIGHT - 1) for x in range(WIDTH)])
    else:
      deep_adj_spaces.append((depth,) + adj)
  return deep_adj_spaces

def adjacent_to(space: tuple) -> list:
  return [
    (space[0] - 1, space[1]),
    (space[0], space[1] - 1),
    (space[0] + 1, space[1]),
    (space[0], space[1] + 1),
  ]

orig_layout = set()
with open(sys.argv[1], "r") as input_file:
  y = 0
  for row in input_file:
    for x in range(len(row)):
      if row[x] == "#":
        orig_layout.add((x, y))
    y += 1

# PART 1
layout = set(orig_layout)
prev_layouts = set()
while frozenset(layout) not in prev_layouts:
  next_layout = set()
  for y in range(HEIGHT):
    for x in range(WIDTH):
      adj_bugs = len([space for space in adjacent_to((x, y)) if space in layout])
      if (x, y) in layout:
        if adj_bugs == 1:
          next_layout.add((x, y))
      else:
        if adj_bugs == 1 or adj_bugs == 2:
          next_layout.add((x, y))

  prev_layouts.add(frozenset(layout))
  layout = next_layout

print(sum([2 ** (space[1] * WIDTH + space[0]) for space in layout]))

# PART 2
deep_layout = set([(0,) + space for space in orig_layout])
for _ in range(200):
  next_layout = set()
  min_depth = min([space[0] for space in deep_layout])
  max_depth = max([space[0] for space in deep_layout])
  for depth in range(min_depth - 1, max_depth + 2):
    for y in range(HEIGHT):
      for x in range(WIDTH):
        if x == y == 2:
          continue
        adj_bugs = len([space for space in deep_adjacent_to((depth, x, y)) if space in deep_layout])
        if (depth, x, y) in deep_layout:
          if adj_bugs == 1:
            next_layout.add((depth, x, y))
        else:
          if adj_bugs == 1 or adj_bugs == 2:
            next_layout.add((depth, x, y))
            
  deep_layout = next_layout

print(len(deep_layout))