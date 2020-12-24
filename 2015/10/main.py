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

def look_and_say(num: int, n: int) -> int:
  """Simulates the look-and-say game to a number n times.

  Arguments:
  num -- the initial number
  n -- the number of iterations
  """
  # Convert num to a string temporarily
  num = str(num)
  for _ in range(n):
    next_turn = ''
    run_start_idx = 0
    idx = 1
    while idx <= len(num):
      if idx == len(num) or num[idx] != num[run_start_idx]:
        next_turn += f'{idx - run_start_idx}{num[run_start_idx]}'
        run_start_idx = idx
      idx += 1
    num = next_turn
  return int(num)

def solve(input_file: typing.IO) -> typing.Generator[any, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  yield len(str(look_and_say(data[0], 40)))
  # WARNING: Part 2 takes several minutes to run!
  yield len(str(look_and_say(data[0], 50)))

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
