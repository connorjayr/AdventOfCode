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

def eval_ye(noparens):
  tokens = noparens.split()
  while '+' in tokens:
    idx = tokens.index('+')
    lhs = int(tokens.pop(idx - 1))
    tokens.pop(idx - 1)
    rhs = int(tokens.pop(idx - 1))
    tokens.insert(idx - 1, lhs + rhs)
  while '*' in tokens:
    idx = tokens.index('*')
    lhs = int(tokens.pop(idx - 1))
    tokens.pop(idx - 1)
    rhs = int(tokens.pop(idx - 1))
    tokens.insert(idx - 1, lhs * rhs)
  return int(tokens[0])
  

def result(line: str) -> int:
  while True:
    new_line = re.sub(r'\(([^\(\)]+)\)', lambda x : str(eval_ye(x.group(1))), line, 1)
    if line == new_line:
      return eval_ye(line)
    else:
      line = new_line

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  # data = split_into_groups([parse_line(line.strip()) for line in input_file])
  acc = 0
  for line in data:
    acc += result(line)
  yield str(acc)

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
