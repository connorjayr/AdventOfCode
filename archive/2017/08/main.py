import collections
import functools
import itertools
import operator
import re
import typing

def run_instructions(registers: dict, instructions: list):
  cond_ops = {
    '<': lambda a, b : a < b,
    '<=': lambda a, b : a <= b,
    '==': lambda a, b : a == b,
    '!=': lambda a, b : a != b,
    '>=': lambda a, b : a >= b,
    '>': lambda a, b : a > b,
  }
  for instruction in instructions:
    reg, op, amnt, cond_reg, cond_op, cond_amnt = list(re.match(r'(.+) ((?:inc)|(?:dec)) (-?\d+) if (.+) ((?:<)|(?:<=)|(?:==)|(?:!=)|(?:>=)|(?:>)) (-?\d+)', instruction).groups())
    if cond_ops[cond_op](registers.get(cond_reg, 0), int(cond_amnt)):
      if op == 'dec':
        registers[reg] = registers.get(reg, 0) - int(amnt)
      elif op == 'inc':
        registers[reg] = registers.get(reg, 0) + int(amnt)

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  data = [line.strip() for line in input_file if line.strip()]
  registers = {}
  run_instructions(registers, data)
  yield str(max(registers.values()))

def main() -> None:
  with open('input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
