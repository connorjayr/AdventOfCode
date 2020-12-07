import collections
import functools
import itertools
import operator
import re
import typing

def unique_houses(directions: str, deliverers: int) -> int:
  locations = [(0, 0)] * deliverers
  deliverer = 0
  houses = set(((0, 0),))
  for direction in directions:
    if direction == '^':
      locations[deliverer] = (locations[deliverer][0], locations[deliverer][1] + 1)
    elif direction == '>':
      locations[deliverer] = (locations[deliverer][0] + 1, locations[deliverer][1])
    elif direction == 'v':
      locations[deliverer] = (locations[deliverer][0], locations[deliverer][1] - 1)
    else:
      locations[deliverer] = (locations[deliverer][0] - 1, locations[deliverer][1])
    houses.add(locations[deliverer])
    deliverer = (deliverer + 1) % deliverers
  return len(houses)

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [line.strip() for line in input_file if line.strip()]
  yield str(unique_houses(data[0], 1))
  yield str(unique_houses(data[0], 2))

def main() -> None:
  """Called when the script is run."""
  with open('input.txt', 'r') as input_file:
    # Print each solution (parts 1 and 2)
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
