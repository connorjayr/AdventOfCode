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

def diff_counter(nums: list) -> collections.Counter:
  """Returns a counter that counts the differences between two consecutive
  numbers in a list.

  Argument:
  nums -- the list of numbers
  """
  counter = collections.Counter()
  for i in range(len(nums) - 1):
    counter[nums[i + 1] - nums[i]] += 1
  return counter

def count_distinct_arrangements(adapters: list):
  """Counts the number of distnct ways in which the adapters may be arranged
  to end up with a final joltage of `adapters[-1]`.

  Arguments:
  adapters -- the adapter outputs
  """
  # ways[idx] corresponds to the following subproblem: how many ways are there
  # to connect adapters to end up with a final joltage of adapters[idx]?
  ways = [0 for _ in range(len(adapters))]
  ways[0] = 1
  for i in range(1, len(ways)):
    j = i - 1
    while j >= 0 and adapters[i] - adapters[j] <= 3:
      ways[i] += ways[j]
      j -= 1
  return ways[-1]

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  data.extend([0, max(data) + 3])
  data.sort()

  diff = diff_counter(data)
  yield str(diff[1] * diff[3])

  yield count_distinct_arrangements(data)

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
