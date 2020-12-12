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

def run_code(code: list, swap_idx: int=0, op_map: dict={}) -> (int, bool):
  """Runs the boot code. Returns a tuple containing the final value of the
  accumulator and a boolean representing whether or not the code terminated
  normally. Swaps the instruction at index `idx` according to the `opMap`
  argument.

  Arguments:
  code -- the boot code
  swap_idx -- the index of the instruction to potentially swap
  op_map - maps operations to others
  """
  # Store the indices of instructions that we have already executed
  visited = set()
  idx = 0
  acc = 0
  while idx not in visited and idx < len(code):
    visited.add(idx)
    op, arg = code[idx].split()
    arg = int(arg)
    if idx == swap_idx:
      # Swap the operation if it exists in the map, otherwise fallback to the
      # original operation
      op = op_map.get(op, op)
    if op == 'acc':
      acc += arg
      idx += 1
    elif op == 'jmp':
      idx += arg
    elif op == 'nop':
      idx += 1
  return (acc, idx == len(code))

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]

  yield str(run_code(data)[0])

  swapResults = [run_code(data, idx, {'jmp': 'nop', 'nop': 'jmp'}) for idx in range(len(data))]
  yield str([result[0] for result in swapResults if result[1]][0])

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
