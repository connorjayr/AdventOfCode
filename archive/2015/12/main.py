import collections
import functools
import itertools
import json
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

def sum_ignore_red(doc: any) -> int:
  """Returns the sum of the numbers in a JSON document. However, numbers that
  are within an object with "red" for any of its values are ignored.

  Arguments:
  doc -- the JSON document
  """
  if isinstance(doc, dict):
    return sum([sum_ignore_red(val) for val in doc.values()]) if 'red' not in doc.values() else 0
  elif isinstance(doc, list):
    return sum([sum_ignore_red(el) for el in doc])
  elif isinstance(doc, int):
    return doc
  else:
    return 0

def solve(input_file: typing.IO) -> typing.Generator[any, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  yield sum([int(num) for num in re.findall(r'-?\d+', data[0])])
  yield sum_ignore_red(json.loads(data[0]))

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
