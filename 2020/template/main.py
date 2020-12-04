import collections
import functools
import itertools
import operator
import re
import typing

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  # data = [line.strip() for line in input_file if line]
  yield 'Solution not implemented'

def main() -> None:
  with open('input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
