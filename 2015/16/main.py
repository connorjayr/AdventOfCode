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

def parse_aunts(lines: list) -> list:
  """Parses the information that could be remembered about the Aunt Sues.

  Arguments:
  lines -- the lines of input
  """
  aunts = []
  for line in lines:
    aunt = {}
    for name, val in re.findall(r'([a-z]+): (\d+)', line):
      aunt[name] = int(val)
    aunts.append(aunt)
  return aunts

def find_match(aunts: list, mfcsam: dict, fn_dict: dict={}) -> int:
  """Finds and returns the number of the Aunt Sue which matches the results from
  the MFCSAM.

  Arguments:
  aunts -- a list of the information for each of the aunts
  mfcsam -- the desired results
  fn_dict -- maps property names to a function to check for a match (optional)
  """
  for idx, aunt in enumerate(aunts):
    match = True
    for name, val in mfcsam.items():
      # Ignore missing properties, and make sure that the ones that do exist
      # have matching values
      if name in aunt and not (fn_dict.get(name, lambda a, b : a == b))(val, aunt[name]):
        match = False
        break
    if match:
      return idx + 1
  return None

def solve(input_file: typing.IO) -> typing.Generator[any, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  aunts = parse_aunts(data)
  yield find_match(aunts, {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
  })
  yield find_match(aunts, {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
  }, {
    'cats': lambda a, b : b > a,
    'trees': lambda a, b : b > a,
    'pomeranians': lambda a, b : b < a,
    'goldfish': lambda a, b : b < a,
  })

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
