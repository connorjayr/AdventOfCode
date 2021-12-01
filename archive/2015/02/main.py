import collections
import functools
import itertools
import operator
import re
import typing

def calc_surface_area(dims: str) -> int:
  """Calculates the total surface area of wrapping paper required to wrap the
  present.

  Arguments:
  dims -- the dimensions of the present: lxwxh
  """
  l, w, h = [int(dim) for dim in dims.split('x')]
  return 2 * (l * w + w * h + h * l) + min(l * w,  w * h, h * l)

def calc_ribbon_length(dims: str) -> int:
  """Calculates the total length of ribbon required for a present.

  Arguments:
  dims -- the dimensions of the present: lxwxh
  """
  dims = sorted([int(dim) for dim in dims.split('x')])
  return 2 * (dims[0] + dims[1]) + functools.reduce(lambda a, b : a * b, dims)

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [line.strip() for line in input_file if line.strip()]
  yield str(sum([calc_surface_area(dims) for dims in data]))
  yield str(sum([calc_ribbon_length(dims) for dims in data]))

def main() -> None:
  """Called when the script is run."""
  with open('input.txt', 'r') as input_file:
    # Print each solution (parts 1 and 2)
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
