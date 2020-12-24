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
  return line

def is_valid(passwd: str) -> bool:
  """Returns true iff a password is valid; i.e., it follows the three given
  rules.

  Arguments:
  passwd - the password
  """
  return (
    re.search(r'abc|bcd|cde|def|efg|fgh|ghi|hij|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz', passwd) is not None and
    all([c not in passwd for c in 'iol']) and
    re.search(r'([a-z])\1.*([a-z])\2', passwd) is not None
  )

def increment_until_valid(passwd: str) -> str:
  """Increments a password until it is valid.

  Arguments:
  passwd -- the current password
  """
  # Convert the password to a list temporarily so we can modify each character
  # individually; reverse the list to make "carrying" in the increment easier
  passwd = list(reversed(passwd))
  while True:
    idx = 0
    # "Carry bit"
    while passwd[idx] == 'z':
      passwd[idx] = 'a'
      idx += 1
    if idx == len(passwd):
      # If the password was originally all z's, then we will have to add an
      # extra character to the beginning of the password
      passwd.append('a')
    else:
      passwd[idx] = chr(ord(passwd[idx]) + 1)

    # Move while condition to end to emulate do-while loop
    if is_valid(''.join(reversed(passwd))): break
  return ''.join(reversed(passwd))

def solve(input_file: typing.IO) -> typing.Generator[any, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  next_passwd = increment_until_valid(data[0])
  yield next_passwd
  yield increment_until_valid(next_passwd)

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
