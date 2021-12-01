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
  return int(line)

def two_sum(nums: list, target: int) -> bool:
  """Returns true iff there exist two distinct numbers in `nums` which sum to
  `target`.

  Argument:
  nums -- the list of numbers
  target -- the target sum
  """
  for a in nums:
    for b in nums:
      if a == b: continue
      if a + b == target: return True
  return False

def find_first_invalid_num(nums: list) -> int:
  """Finds the first invalid number in a list of numbers; i.e., the first number
  which cannot be expressed as a sum of any two of the previous 25 numbers.

  Arguments:
  nums -- the list of numbers
  """
  for idx in range(25, len(nums)):
    if not two_sum(nums[idx - 25:idx], nums[idx]):
      return nums[idx]
  return None

def find_encryption_weakness(nums, invalid_num):
  """Finds the encryption weakness in a list of numbers; i.e., the minimum plus
  the maximum of a contiguous set of at least two numbers which add up to the
  first invalid number found using the above method.

  Arguments:
  nums -- the list of numbers
  invalid_num -- the first invalid number found using the above method
  """
  for start in range(len(nums)):
    for end in range(start + 2, len(nums)):
      sublist = nums[start:end]
      if sum(sublist) == invalid_num:
        return min(sublist) + max(sublist)
  return None

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]

  first_invalid_num = find_first_invalid_num(data)
  yield str(first_invalid_num)

  yield str(find_encryption_weakness(data, first_invalid_num))

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
