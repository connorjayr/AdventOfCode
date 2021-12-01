import typing

def move(pos: tuple, direction: tuple) -> tuple:
  """Moves to a position one unit in a given direction.

  Arguments:
  pos -- the starting position
  direction -- the direction to move
  """
  return tuple([pos[idx] + direction[idx] for idx in range(len(pos))])

def adjacent_sum(grid: dict, pos: tuple) -> int:
  """Calculates the sum of the values in the squares adjacent to a given
  position.

  Arguments:
  grid -- the grid of values
  pos -- the position
  """
  adj_sum = 0
  for dx in range(-1, 2):
    for dy in range(-1, 2):
      if dx == 0 and dy == 0: continue
      adj_sum += grid.get((pos[0] + dx, pos[1] + dy), 0)
  return adj_sum

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  start_square = int(input_file.readline().strip())

  # PART 1
  radius = 0
  while (2 * radius + 1) ** 2 < start_square:
    radius += 1
  square = (2 * radius + 1) ** 2

  # Move clockwise around the grid to find the value at the appropriate radius
  pos = (radius, radius)
  while square != start_square:
    if pos[0] > -radius and pos[1] == radius:
      pos = (pos[0] - 1, pos[1])
    elif pos[0] == -radius:
      pos = (pos[0], pos[1] - 1)
    elif pos[1] == -radius:
      pos = (pos[0] + 1, pos[1])
    else:
      pos = (pos[0], pos[1] + 1)
    square -= 1
  yield str(sum([abs(dim) for dim in pos]))

  # PART 2
  grid = {(0, 0): 1}
  pos = (0, 0)
  dirs = ((1, 0), (0, -1), (-1, 0), (0, 1))
  dir_idx = 0
  while grid[pos] <= start_square:
    pos = move(pos, dirs[dir_idx])
    grid[pos] = adjacent_sum(grid, pos)
    # wrote grid[]

    # If we can turn left, do so
    left_idx = (dir_idx + 1) % len(dirs)
    if move(pos, dirs[left_idx]) not in grid:
      dir_idx = left_idx
  yield str(grid[pos])

def main() -> None:
  with open('input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
