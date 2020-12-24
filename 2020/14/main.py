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

def mask_num(num, mask):
  print(num, mask)
  result = ''
  for i in range(len(num)):
    if mask[i] == '1' or mask[i] == 'X':
      result += mask[i]
    else:
      result += num[i]
  return result

def generate_nums(val):
  nums = []
  for ye in itertools.product('10', repeat=val.count('X')):
    print(ye)
    idx = 0
    num = ''
    for c in val:
      if c == 'X':
        num += ye[idx]
        idx += 1
      else:
        num += c
    print(num)
    nums.append(int(num, 2))
  print(nums)
  return nums

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
  mask = 'X' * 36
  mem = {}
  for line in data:
    if line.startswith('mask = '):
      mask = line[7:]
    else:
      address, val = list(re.match(r'mem\[(\d+)\] = (\d+)', line).groups())
      address = int(address)
      add_str = '{0:b}'.format(address)
      add_str = '0' * (36 - len(add_str)) + add_str
      val = int(val)
      # val_str = '{0:b}'.format(val)
      # mem[address] = mask_num('0' * (36 - len(val_str)) + val_str, mask)
      print(add_str)
      for add in generate_nums(mask_num(add_str, mask)):
        mem[add] = val
  print(mem)
  yield str(sum(mem.values()))

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
