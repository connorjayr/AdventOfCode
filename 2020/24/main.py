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

def count_live(flipped, pos):
  count = 0
  for offset in ((-1,0),(-1,1),(0,1),(1,0),(1,-1),(0,-1)):
    if (pos[0] + offset[0], pos[1] + offset[1]) in flipped:
      count += 1
  return count

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  flipped = set()
  for line in data:
    pos = (0, 0)
    while line:
      direction = line[0]
      line = line[1:]
      if direction == 'n' or direction == 's':
        direction += line[0]
        line = line[1:]
      if direction == 'w':
        pos = (pos[0], pos[1] - 1)
      elif direction == 'nw':
        pos = (pos[0] - 1, pos[1])
      elif direction == 'ne':
        pos = (pos[0] - 1, pos[1] + 1)
      elif direction == 'sw':
        pos = (pos[0] + 1, pos[1] - 1)
      elif direction == 'se':
        pos = (pos[0]  +1 , pos[1])
      elif direction == 'e':
        pos = (pos[0], pos[1] + 1)
    if pos in flipped:
      flipped.remove(pos)
    else:
      flipped.add(pos)
  yield str(len(flipped))

  for _ in range(100):
    candidates = set()
    next_flipped = set()
    for pos in flipped:
      for offset in ((-1,0),(-1,1),(0,1),(1,0),(1,-1),(0,-1)):
        candidates.add((pos[0] + offset[0], pos[1] + offset[1]))
    for candidate in candidates:
      count = count_live(flipped, candidate)
      if candidate in flipped and not (count == 0 or count > 2):
        next_flipped.add(candidate)
      elif candidate not in flipped and count == 2:
        next_flipped.add(candidate)
    flipped = next_flipped
    print(len(flipped))
  print(len(flipped))

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
