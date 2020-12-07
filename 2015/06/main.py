import collections
import functools
import itertools
import operator
import re
import typing

def run_instructions(grid: list, instructions: list, ops: dict) -> None:
  for instruction in instructions:
    op, min_row, min_col, max_row, max_col = list(re.match(r'((?:turn on)|(?:turn off)|(?:toggle)) (\d+),(\d+) through (\d+),(\d+)', instruction).groups())
    for row in range(int(min_row), int(max_row) + 1):
      for col in range(int(min_col), int(max_col) + 1):
        grid[row][col] = ops[op](grid[row][col])

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [line.strip() for line in input_file if line.strip()]
  
  grid = [[False for _ in range(1000)] for _ in range(1000)]
  run_instructions(grid, data, {
    'turn on': lambda a : True,
    'turn off': lambda a : False,
    'toggle': lambda a : not a,
  })
  yield str(sum([row.count(True) for row in grid]))

  grid = [[0 for _ in range(1000)] for _ in range(1000)]
  run_instructions(grid, data, {
    'turn on': lambda a : a + 1,
    'turn off': lambda a : max(a - 1, 0),
    'toggle': lambda a : a + 2,
  })
  yield str(sum([sum(row) for row in grid]))

def main() -> None:
  """Called when the script is run."""
  with open('input.txt', 'r') as input_file:
    # Print each solution (parts 1 and 2)
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
