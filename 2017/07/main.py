import collections
import functools
import itertools
import operator
import re
import typing

def construct_tower(lines: str) -> tuple:
  tower = {}
  weights = {}
  for line in lines:
    if '->' in line:
      name, weight, programs_above = list(re.match(r'(.+) \((\d+)\) -> (.+)', line).groups())
      tower[name] = programs_above.split(', ')
      weights[name] = weight
    else:
      name, weight = list(re.match(r'(.+) \((\d+)\)', line).groups())
      tower[name] = []
      weights[name] = weight
  return tower, weights

def find_bottom(tower: dict) -> str:
  above_bottom = set()
  for programs_above in tower.values():
    for program in programs_above:
      above_bottom.add(program)
  return list(set(tower.keys()).difference(above_bottom))[0]

def calc_stack_weight(tower: dict, weights: dict, program: str) -> int:
  return weights[program] + sum([calc_stack_weight(program_above) for program_above in tower[program]])

def fix_weight(tower: dict, weights: dict, program: str) -> int:
  stacks = set()
  for program_above in tower[program]:
    stack = calc_stack_weight(tower, weights, program_above)
    if stacks and stack not in stacks:
      return fix_weight(tower, weights, program_above)
  # TODO

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  data = [line.strip() for line in input_file if line.strip()]
  tower, weights = construct_tower(data)
  bottom = find_bottom(tower)
  yield bottom
  yield fix_weight(tower, weights, bottom)

def main() -> None:
  with open('input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
