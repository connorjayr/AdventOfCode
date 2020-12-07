import collections
import functools
import itertools
import operator
import re
import typing

def has_duplicate_letter(string: str) -> bool:
  """Returns True iff a string has a letter that occurs twice in a row.

  Arguments:
  string -- the string
  """
  for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
      return True
  return False

def is_nice(string: str) -> bool:
  """Returns True iff a string is nice.

  Arguments:
  string -- the string
  """
  return (
    re.search(r'[aeiou].*[aeiou].*[aeiou]', string) is not None and
    re.search(r'(.)\1', string) is not None and
    all([substring not in string for substring in ['ab', 'cd', 'pq', 'xy']])
  )

def is_nice_better(string: str) -> bool:
  """Returns True iff a string is nice using the better model.

  Arguments:
  string -- the string
  """
  return (
    re.search(r'(.{2}).*\1', string) is not None and
    re.search(r'(.).\1', string) is not None
  )

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [line.strip() for line in input_file if line.strip()]
  yield str([is_nice(string) for string in data].count(True))
  yield str([is_nice_better(string) for string in data].count(True))

def main() -> None:
  """Called when the script is run."""
  with open('input.txt', 'r') as input_file:
    # Print each solution (parts 1 and 2)
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
