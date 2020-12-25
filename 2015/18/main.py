import collections
import functools
import itertools
import math
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

def parse_initial_configuration(lines: list) -> set:
  """Parses the initial configuration of lights. Returns a set containing the
  coordiantes of lights that are turned on.

  Arguments:
  lines -- the lines to parse
  """
  on = set()
  for y in range(len(lines)):
    for x in range(len(lines[y])):
      if lines[y][x] == '#':
        on.add((x, y))
  return on

def is_in_bounds(coordinate: tuple) -> bool:
  return all(0 <= c < 100 for c in coordinate)

def get_neighbors(coordinate: tuple) -> list:
  return [tuple(coordinate[idx] + offset[idx] for idx in range(len(coordinate))) for offset in itertools.product((-1, 0, 1), repeat=len(coordinate)) if not all(o == 0 for o in offset) and is_in_bounds(tuple(coordinate[idx] + offset[idx] for idx in range(len(coordinate))))]

def advance(on: set, fixed: list=[]) -> set:
  """Advances a configuration of lights to the next step.

  Arguments:
  on -- contains coordinates of lights that are turned on
  fixed -- a list of coordinates of lights that are always turned on (optional)
  """
  on |= set(fixed)
  next_step = set()
  candidates = set(sum((get_neighbors(coordinate) for coordinate in on), []))
  for candidate in candidates:
    on_neighbors = [neighbor in on for neighbor in get_neighbors(candidate)].count(True)
    if candidate in on and 2 <= on_neighbors <= 3:
      next_step.add(candidate)
    elif candidate not in on and on_neighbors == 3:
      next_step.add(candidate)
  return next_step | set(fixed)

def solve(input_file: typing.IO) -> typing.Generator[any, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  init = parse_initial_configuration(data)

  on = init
  for step in range(100):
    on = advance(on)
  yield len(on)

  on = init
  for step in range(100):
    on = advance(on, list(itertools.product((0, 99), repeat=2)))
  yield len(on)

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
