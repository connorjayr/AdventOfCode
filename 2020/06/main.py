from ..util.inputs import *
import collections
import functools
import itertools
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

def count_anyone_answered(group: list) -> int:
  """Counts the total number of questions that anyone answered "yes" to in a
  group.

  Arguments:
  group -- the questions that each person in the group answered "yes" to
  """
  return len(functools.reduce(lambda a, b : a + b, [collections.Counter(answers) for answers in group]))

def count_everyone_answered(group: list) -> int:
  """Counts the total number of questions that everyone answered "yes" to in a
  group.

  Arguments:
  group -- the questions that each person in the group answered "yes" to
  """
  return len(functools.reduce(lambda a, b : a & b, [collections.Counter(answers) for answers in group]))

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = split_into_groups([parse_line(line.strip()) for line in input_file])
  yield str(sum([count_anyone_answered(group) for group in data]))
  yield str(sum([count_everyone_answered(group) for group in data]))

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
