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

def parse_relationships(lines: list) -> dict:
  """Parses the relationships between pairs of people.

  Arguments:
  lines -- the lines describing the relationships
  """
  relationships = collections.defaultdict(dict)
  for line in lines:
    tokens = line[:-1].split()
    relationships[tokens[0]][tokens[-1]] = (1 if tokens[2] == 'gain' else -1) * int(tokens[3])
  return relationships

def total_happiness(relationships: dict, arrangement: list) -> int:
  """Returns the total happiness of the people at the dinner table with the
  given arrangement.

  Arguments:
  relationships -- maps pairs of people to the happiness gained or lost by the
  first person if the second person is sitting next to them
  arrangement -- the arrangement of people at the dinner table
  """
  total = 0
  for idx in range(len(arrangement)):
    neighbors = [arrangement[(idx + offset) % len(arrangement)] for offset in (-1, 1)]
    total += sum(relationships[arrangement[idx]].get(neighbor, 0) for neighbor in neighbors)
  return total

def find_optimal_arrangement(relationships: dict) -> int:
  """Finds the optimal arrangement of the dinner table and returns the total
  happiness for this arrangement.

  Arguments:
  relationships -- maps pairs of people to the happiness gained or lost by the
  first person if the second person is sitting next to them
  """
  return max(total_happiness(relationships, arrangement) for arrangement in itertools.permutations(relationships.keys(), len(relationships)))

def solve(input_file: typing.IO) -> typing.Generator[any, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  relationships = parse_relationships(data)
  yield find_optimal_arrangement(relationships)
  relationships['me'] = {}
  yield find_optimal_arrangement(relationships)

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
