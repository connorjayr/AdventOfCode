from ..util.inputs import *
import collections
import functools
import itertools
import networkx as nx
import operator
import os
import re
import sys
import typing

def parse_line(line: str) -> str:
  """Parses a line of input. By default, does nothing.

  Arguments:
  line -- the line of input
  """
  return list(line)

def count_adjacent_occupied_seats(grid: list, pos: tuple, ignore_floor: bool) -> int:
  """Counts the number of occupied seats that are adjacent (horizontally,
  vertically, or diagonally) to the given position.

  Arguments:
  grid -- the two-dimensional grid
  pos -- the position
  ignore_floor -- `True` iff floor squares should be ignored when searching for
  adjacent seats
  """
  occupied_seats = 0
  for step in ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)):
    if ignore_floor:
      dist = 1
      while True:
        # Keep incrementing `dist` until we reach a seat or the edge of the
        # board
        dest = (pos[0] + step[0] * dist, pos[1] + step[1] * dist)
        if not (0 <= dest[1] < len(grid) and 0 <= dest[0] < len(grid[dest[1]])) or grid[dest[1]][dest[0]] == 'L':
          break
        elif grid[dest[1]][dest[0]] == '#':
          occupied_seats += 1
          break
        dist += 1
    else:
      dest = (pos[0] + step[0], pos[1] + step[1])
      if 0 <= dest[1] < len(grid) and 0 <= dest[0] < len(grid[dest[1]]) and grid[dest[1]][dest[0]] == '#':
        occupied_seats += 1
  return occupied_seats

def advance_until_stable(grid: list, overpopulation_threshold: int, ignore_floor: bool) -> int:
  """Returns the number of occupied seats after advancing the grid to the next
  generation until it is stable; i.e., it does not change from generation to
  generation.

  Arguments:
  grid -- the initial grid
  overpopulation_threshold -- the number of occupied adjacent seats for an
  occupied seat to become empty again
  ignore_floor -- whether or not floor squares should be ignored when checking
  adjacent seats
  """
  # Store which states have already been seen
  seen = set()
  while tuple(tuple(row) for row in grid) not in seen:
    seen.add(tuple(tuple(row) for row in grid))
    next_grid = [list(row) for row in grid]
    for y in range(len(grid)):
      for x in range(len(grid[y])):
        adjacent_occupied_seats = count_adjacent_occupied_seats(grid, (x, y), ignore_floor)
        if grid[y][x] == 'L' and adjacent_occupied_seats == 0:
          next_grid[y][x] = '#'
        elif grid[y][x] == '#' and adjacent_occupied_seats >= overpopulation_threshold:
          next_grid[y][x] = 'L'
    grid = next_grid
  return sum([row.count('#') for row in grid])

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  yield str(advance_until_stable(data, 4, False))
  yield str(advance_until_stable(data, 5, True))

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
