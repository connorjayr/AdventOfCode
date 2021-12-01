import collections
import functools
import itertools
import operator
import re
import typing

def count_trees(tree_map: list, step: tuple) -> int:
  """Counts the number of trees that the toboggan would encouter when starting
  at a given position and moving by a fixed step vector.

  Arguments:
  tree_map -- the two-dimensional map indicating where trees are
  step -- the vector indicating the toboggan's movement
  """
  trees = 0
  # Ignore (0, 0)
  pos = step
  # Iterate until we reach the bottom row
  while pos[1] < len(tree_map):
    if tree_map[pos[1]][pos[0]] == '#':
      trees += 1
    # Move the position by the step, using mod to "repeat" the map to the right
    pos = ((pos[0] + step[0]) % len(tree_map[pos[1]]), pos[1] + step[1])
  return trees

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  data = [line.strip() for line in input_file if line]
  yield str(count_trees(data, (3, 1)))
  yield str(functools.reduce(operator.mul, [count_trees(data, step) for step in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]))

def main() -> None:
  with open('input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
