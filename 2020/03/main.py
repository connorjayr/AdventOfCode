import functools
import operator
import typing

def count_trees(tree_map: list, step: tuple) -> int:
  trees = 0
  pos = (0, 0)
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
