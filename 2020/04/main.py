import collections
import functools
import itertools
import operator
import re
import typing

def parse_passports(lines: list) -> list:
  """Parses the lines of an input file for passports.
  
  Arguments:
  lines -- the lines of the input file
  """
  # Add an extra newline in case the input file doesn't have a terminating
  # newline
  lines.append('\n')

  passports = []
  # Store the fields of the current passport
  curr_passport = {}
  for line in lines:
    if not line.strip():
      # We have reached an empty line, which marks the end of a passport
      passports.append(curr_passport)
      curr_passport = {}
    else:
      for field in line.strip().split(' '):
        key, value = field.split(':')
        curr_passport[key] = value
  return passports

def has_required_fields(passport: dict) -> bool:
  """Returns true iff a passport, represented as a dictionary, has all of the
  required fields.

  Arguments:
  passport -- the key-value pairs that make up the passport
  """
  return all([key in passport for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']])

def is_valid(passport: dict) -> bool:
  """Returns true iff a passport is valid; i.e., it has all of the required
  fields and the values for the fields are valid according to the rules.

  Arguments:
  passport -- the key-value pairs that make up the passport
  """
  return (
    has_required_fields(passport) and
    re.match(r'^\d{4}$', passport['iyr']) is not None and 2010 <= int(passport['iyr']) <= 2020 and
    re.match(r'^\d{4}$', passport['eyr']) is not None and 2020 <= int(passport['eyr']) <= 2030 and
    re.match(r'^\d{4}$', passport['byr']) is not None and 1920 <= int(passport['byr']) <= 2002 and
    (
      (passport['hgt'].endswith('cm') and 150 <= int(passport['hgt'][:-2]) <= 193) or
      (passport['hgt'].endswith('in') and 59 <= int(passport['hgt'][:-2]) <= 76)
    ) and
    re.match(r'^#[\da-f]{6}$', passport['hcl']) is not None and
    passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and
    re.match(r'^\d{9}$', passport['pid']) is not None
  )

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  passports = parse_passports(input_file.readlines())
  yield str([has_required_fields(passport) for passport in passports].count(True))
  yield str([is_valid(passport) for passport in passports].count(True))

def main() -> None:
  with open('input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
