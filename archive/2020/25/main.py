from ..util.inputs import *
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

def transform(subject_num, loop_size):
  return 

def solve(input_file: typing.IO) -> typing.Generator[any, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  card_loop_size = 3974372
  while pow(7, card_loop_size, 20201227) != data[0]:
    card_loop_size += 1
  door_loop_size = 8623737
  while pow(7, door_loop_size, 20201227) != data[1]:
    door_loop_size += 1
  print(pow(data[1], card_loop_size, 20201227))

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
