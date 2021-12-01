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

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  cups = [int(n) for n in list(data[0])]
  min_cup = min(cups)
  max_cup = max(cups)
  # current_label = cups[0]
  while len(cups) < 1000000:
    cups.append(max_cup + 1)
    max_cup += 1
  current_idx = 0
  for i in range(10000000):
    # print(cups, current_label)
    # current = cups.index(current_label)
    # print('idx', current)
    pop_idx = (current_idx + 3) % len(cups)
    if pop_idx < current_idx:
      current_idx -= 1
    r3 = cups.pop(pop_idx)
    pop_idx = (current_idx + 2) % len(cups)
    if pop_idx < current_idx:
      current_idx -= 1
    r2 = cups.pop(pop_idx)
    pop_idx = (current_idx + 1) % len(cups)
    if pop_idx < current_idx:
      current_idx -= 1
    r1 = cups.pop(pop_idx)
    # print(r1, r2, r3)
    dest_label = cups[current_idx] - 1
    while dest_label in (r1, r2, r3) or dest_label < min_cup:
      dest_label -= 1
      if dest_label < min_cup:
        dest_label = max_cup
    # print(dest_label)
    dest = cups.index(dest_label)
    cups.insert(dest + 1, r3)
    cups.insert(dest + 1, r2)
    cups.insert(dest + 1, r1)
    current_idx = (current_idx + 1) % len(cups)
    if i % 100 == 0:
      print(i)
  print(cups[(cups.index(1) + 1) % len(cups)] * cups[(cups.index(1) + 2) % len(cups)])

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
