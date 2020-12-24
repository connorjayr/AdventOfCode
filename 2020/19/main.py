from ..util.inputs import *
import collections
import functools
import itertools
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

def parse_rules(rule_list: list) -> dict:
  rules = {}
  for rule in rule_list:
    source, dest = list(re.match(r'(\d+): (.+)', rule).groups())
    if '"' in dest:
      rules[int(source)] = dest[1]
    else:
      rules[int(source)] = [[int(subrule) for subrule in subrule_list.split()] for subrule_list in dest.split(' | ')]
  return rules

def gen_regexp(rules: dict, rule: int) -> str:
  if rule == 8:
    return gen_regexp(rules, 42) + '+'
  elif rule == 11:
    lhs = gen_regexp(rules, 42)
    rhs = gen_regexp(rules, 31)
    return '(?:' + '|'.join(f'(?:{lhs}{{{n}}}{rhs}{{{n}}})' for n in range(1, 100)) + ')'
  elif isinstance(rules[rule], str): return rules[rule]
  else: return '(?:' + '|'.join([''.join([gen_regexp(rules, subrule) for subrule in subrule_list]) for subrule_list in rules[rule]]) + ')'

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  # data = [parse_line(line.strip()) for line in input_file if line.strip()]
  data = split_into_groups([line.strip() for line in input_file])
  rules = parse_rules(data[0])
  regexp = gen_regexp(rules, 0)
  yield str([re.fullmatch(regexp, msg) is not None for msg in data[1]].count(True))

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
