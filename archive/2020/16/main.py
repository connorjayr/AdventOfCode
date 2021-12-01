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

def parse_rules(lines: list, rules: dict):
  """Parses lines for rules regarding passport fields.

  Arguments:
  lines -- lines from the input file corresponding to the rules
  rules -- maps field names to bounds; modified by this method
  """
  for line in lines:
    field, *bounds = list(re.match(r'([a-z ]+): (\d+)\-(\d+) or (\d+)\-(\d+)', line).groups())
    rules[field] = [int(bound) for bound in bounds]

def calc_error_rate(tickets: list, rules: dict) -> int:
  """Calculates the "ticket scanning error rate" for a list of tickets; i.e., a
  sum of the invalid values.
  
  Arguments:
  tickets -- the nearby tickets
  rules -- maps field names to bounds
  """
  return sum([sum([val for val in ticket if not any([bounds[0] <= val <= bounds[1] or bounds[2] <= val <= bounds[3] for bounds in rules.values()])]) for ticket in tickets])

def find_valid_fields(rules, vals) -> list:
  """Returns a list of fields for which the given values are valid.

  Arguments:
  rules -- maps field names to bounds
  vals -- the values for a particular (unknown) field on the nearby tickets
  """
  return [field for field, bounds in rules.items() if all([bounds[0] <= val <= bounds[1] or bounds[2] <= val <= bounds[3] for val in vals])]

def decode_fields(tickets: list, rules: dict):
  """Decodes the order of fields on the nearby passports.
  
  Arguments:
  tickets -- the nearby tickets
  rules -- maps field names to bounds
  """
  # Make a copy to avoid modifying the original dict
  rules = dict(rules)
  tickets = [ticket for ticket in tickets if all([any([bounds[0] <= val <= bounds[1] or bounds[2] <= val <= bounds[3] for bounds in rules.values()]) for val in ticket])]
  fields = [None] * len(tickets[0])
  while None in fields:
    for idx in range(len(fields)):
      # Ignore any fields which we have already decoded
      if fields[idx] is not None: continue
      # Collect a set of values for this field from all of the nearby tickets
      vals = set([ticket[idx] for ticket in tickets])
      valid_fields = find_valid_fields(rules, vals)
      if len(valid_fields) == 1:
        fields[idx] = valid_fields[0]
        del rules[valid_fields[0]]
  return fields 

def valid_for_fields(rules, vals):
  valid = []
  for field, rule in rules.items():
    if all([(rule[0] <= val <= rule[1] or rule[2] <= val <= rule[3]) for val in vals]): valid.append(field)
  return valid

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = split_into_groups([parse_line(line.strip()) for line in input_file])

  rules = {}
  parse_rules(data[0], rules)
  my_ticket = [int(val) for val in data[1][1].split(',')]
  nearby_tickets = [[int(val) for val in line.split(',')] for line in data[2][1:]]

  yield calc_error_rate(nearby_tickets, rules)
  yield functools.reduce(lambda a, b : a * b, [my_ticket[idx] for idx, field in enumerate(decode_fields(nearby_tickets, rules)) if field.startswith('departure')])

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
