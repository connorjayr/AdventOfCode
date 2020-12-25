from ..util.inputs import split_into_groups
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

def make_replacements(molecule: str, replacements: list) -> set:
  """Makes replacements on the given molecule and returns the unique molecules
  that result from these replacements.

  Arguments:
  molecule -- the initial molecule
  replacements -- the replacement rules
  """
  results = set()
  for replacement in replacements:
    start_idx = 0
    while (start_idx := molecule.find(replacement[0], start_idx)) != -1:
      results.add(molecule[:start_idx] + replacement[1] + molecule[start_idx + len(replacement[0]):])
      start_idx += 1
  return results

def bfs(start: str, replacements: list, target: str) -> int:
  """Performs a BFS traversal to find the lowest number of replacements needed
  to obtain the target molecule from the starting molecule.

  Arguments:
  start -- the starting molecule
  replacements -- the replacement rules
  target -- the target molecule
  """
  visited = set([start])
  # Store the current molecule as well as the number of replacements made to
  # obtain that molecule
  queue = [(start, 0)]
  while queue:
    curr = queue.pop(0)
    if curr[0] == target:
      return curr[1]
    neighbors = make_replacements(curr[0], replacements)
    for neighbor in neighbors:
      if neighbor in visited: continue
      visited.add(neighbor)
      queue.append((neighbor, curr[1] + 1))

def solve(input_file: typing.IO) -> typing.Generator[any, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = split_into_groups([parse_line(line.strip()) for line in input_file])

  replacements = [line.split(' => ') for line in data[0]]
  yield len(make_replacements(data[1][0], replacements))

  # WARNING: Part 2 does not run in a reasonable amount of time (yet)
  reverse_replacements = [list(reversed(replacement)) for replacement in replacements]
  yield bfs(data[1][0], reverse_replacements, 'e')

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
