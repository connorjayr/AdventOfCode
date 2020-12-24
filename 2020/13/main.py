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

def chinese_remainder(n, a):
  sum = 0
  prod = functools.reduce(lambda a, b: a*b, n)
  for n_i, a_i in zip(n, a):
      p = prod // n_i
      sum += a_i * mul_inv(p, n_i) * p
  return sum % prod
 
def mul_inv(a, b):
  b0 = b
  x0, x1 = 0, 1
  if b == 1: return 1
  while a > 1:
      q = a // b
      a, b = b, a%b
      x0, x1 = x1 - q * x0, x0
  if x1 < 0: x1 += b0
  return x1

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  me = int(data[0])
  busses = [int(bus) for bus in data[1].split(',') if bus != 'x']
  nearest = min([(bus - (me % bus), bus) for bus in busses], key=lambda x : x[0])
  print(nearest[0], me + nearest[0], nearest[1])
  yield nearest[0] * nearest[1]

  a = [int(bus) - offset for offset, bus in enumerate(data[1].split(',')) if bus != 'x']
  
  print(busses, a)
  yield chinese_remainder(busses, a)

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
