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
  return line

def count_active_neighbors(active: set, pt: tuple) -> int:
  """Counts the number of active neighbors to the given point.

  Arguments:
  active -- contains the active points
  pt -- the point whose neighors are under consideration
  """
  return [tuple(pt[idx] + offset[idx] for idx in range(len(pt))) in active for offset in itertools.product((-1, 0, 1), repeat=len(pt))].count(True)

def simulate_next_cycle(active: set, dims: int) -> set:
  """Simluates a cycle.

  Arguments:
  active -- contains the active points
  dims -- the number of dimensions in space
  """
  # Candidate points are any cube adjacent to an active cube (or the active cube
  # itself)
  candidates = set(tuple(pt[idx] + offset[idx] for idx in range(dims)) for pt in active for offset in itertools.product((-1, 0, 1), repeat=dims))
  return set(pt for pt in candidates if (pt in active and 2 <= count_active_neighbors(active, pt) <= 3) or (pt not in active and count_active_neighbors(active, pt) == 3))

def count_active_after_n_cycles(init_grid: list, n: int, dims: int) -> int:
  """Counts the number of active cubes after n cycles.
  
  Arguments:
  init_grid -- the initial state of the grid; '#' represents an active cube
  n -- the number of cycles that will be simulated
  dims -- the number of dimensions in space
  """
  active = set((x, y) + (0,) * (dims - 2) for y in range(len(init_grid)) for x in range(len(init_grid[y])) if init_grid[y][x] == '#')
  for _ in range(n):
    active = simulate_next_cycle(active, dims)
  return len(active)

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  yield str(count_active_after_n_cycles(data, 6, 3))
  yield str(count_active_after_n_cycles(data, 6, 4))

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
