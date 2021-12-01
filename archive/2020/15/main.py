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

def get_nth_number(starting_nums: list, n: int) -> int:
  """Returns the nth number spoken in the memory game.

  Arguments:
  starting_nums -- the starting numbers
  n -- the position of the returned number
  """
  last_idx = {}
  # Index the starting numbers
  for idx in range(len(starting_nums)):
    last_idx[starting_nums[idx]] = idx
  
  next_num = starting_nums[-1]
  for idx in range(len(starting_nums), n + 1):
    curr_num = next_num
    if next_num in last_idx:
      next_num = idx - last_idx[curr_num]
    else:
      next_num = 0
    last_idx[curr_num] = idx
  return curr_num

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  starting_nums = [int(num) for num in data[0].split(',')]
  yield get_nth_number(starting_nums, 2020)
  yield get_nth_number(starting_nums, 30000000)
  for idx, num in enumerate(nums):
    last_idx[num].append(idx)
  while len(nums) < 30000000:
    prev = nums[-1]
    if len(last_idx[prev]) <= 1:
      nums.append(0)
    else:
      nums.append(last_idx[prev][-1] - last_idx[prev][-2])
    last_idx[nums[-1]].append(len(nums) - 1)
    if len(nums) % 100000 == 0:
      print(len(nums))
  yield nums[-1]
def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
