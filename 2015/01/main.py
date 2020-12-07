import collections
import functools
import itertools
import operator
import re
import typing

def first_basement_position(instructions: str) -> int:
  """Finds the first character position which results in Santa entering the
  basement.

  Arguments:
  instructions -- the instructions that tell Santa to go up or down one floor
  """
  floor = 0
  for pos, char in enumerate(instructions):
    if char == '(':
      floor += 1
    else:
      floor -= 1
    if floor == -1: return pos + 1

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [line.strip() for line in input_file if line.strip()]
  yield str(sum([1 if char == '(' else -1 for char in data[0]]))
  yield str(first_basement_position(data[0]))

def main() -> None:
  """Called when the script is run."""
  with open('input.txt', 'r') as input_file:
    # Print each solution (parts 1 and 2)
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
