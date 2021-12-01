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

def recurse(p1, p2):
  seen = set()
  # print('init:', p1, p2, (tuple(p1), tuple(p2)) in seen)
  # print(seen)
  while (tuple(p1), tuple(p2)) not in seen:
    # print(p1, p2)
    if len(p1) == 0: return 2
    elif len(p2) == 0: return 1

    seen.add((tuple(p1), tuple(p2)))

    t1 = p1.pop(0)
    t2 = p2.pop(0)
    if t1 <= len(p1) and t2 <= len(p2):
      # print('recurse...', list(p1[:t1]))
      winner = recurse(list(p1[:t1]), list(p2[:t2]))
      if winner == 1:
        p1.extend([t1, t2])
      else:
        p2.extend([t2, t1])
    else:
      if t1 > t2:
        p1.extend([t1, t2])
      else:
        p2.extend([t2, t1])
  return 1

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = split_into_groups([parse_line(line.strip()) for line in input_file])
  p1 = [int(n) for n in data[0][1:]]
  p2 = [int(n) for n in data[1][1:]]
  # while len(p1) > 0 and len(p2) > 0:
  #   t1 = p1.pop(0)
  #   t2 = p2.pop(0)
  #   if t1 > t2:
  #     p1.extend([t1, t2])
  #   elif t2 > t1:
  #     p2.extend([t2, t1])
  #   else:
  #     assert False
  # winner = p1 if len(p1) > 0 else p2
  seen = set()
  winner_num = recurse(p1, p2)
  winner = p1 if winner_num == 1 else p2
  print(p1, p2)
  yield sum([(len(winner) - idx) * card for idx, card in enumerate(winner)])
  

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
