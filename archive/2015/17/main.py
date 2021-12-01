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
  return int(line)

def count_combinations(sizes: list, target: int, remaining: float=math.inf) -> int:
  """Counts the number of combinations of containers to obtain the target size.

  Arguments:
  sizes -- the container sizes
  target -- the target size
  remaining -- the number of remaining containers that may be used (optional)
  """
  if target == 0: return 1
  if len(sizes) == 0 or target < 0 or remaining <= 0: return 0
  return count_combinations(sizes[1:], target, remaining=remaining) + count_combinations(sizes[1:], target - sizes[0], remaining=remaining - 1)

def solve(input_file: typing.IO) -> typing.Generator[any, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  
  yield count_combinations(data, 150, math.inf)

  remaining = 1
  while True:
    count = count_combinations(data, 150, remaining=remaining)
    if count > 0:
      yield count
      break
    remaining += 1

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
