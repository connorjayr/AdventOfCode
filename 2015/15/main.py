import collections
import functools
import itertools
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

def parse_ingredients(lines: list) -> dict:
  """Parses ingredients from an input file.

  Arguments:
  lines -- the lines of input
  """
  ingredients = {}
  for line in lines:
    name, c, d, f, t, cal = list(re.fullmatch(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line).groups())
    ingredients[name] = tuple(int(val) for val in (c, d, f, t, cal))
  return ingredients

def calc_max_score(ingredients: dict, tsp: int, cals: int=None) -> int:
  """Calculates the maximum score for a combination of a given number of
  teaspoons of ingredients.

  Arguments:
  ingredients -- maps ingredient names to their properties
  tsp -- the total number of teaspoons
  cals -- the number of calories that the resulting combination must have
  (optional)
  """
  ingr_list = list(ingredients.keys())
  max_score = -math.inf
  for a in range(tsp + 1):
    for b in range(tsp + 1 - a):
      for c in range(tsp + 1 - a - b):
        d = tsp - a - b - c
        if cals is None or a * ingredients[ingr_list[0]][4] + b * ingredients[ingr_list[1]][4] + c * ingredients[ingr_list[2]][4] + d * ingredients[ingr_list[3]][4] == cals:
          max_score = max(max_score, functools.reduce(lambda a, b : a * b, (max(0, a * ingredients[ingr_list[0]][prop] + b * ingredients[ingr_list[1]][prop] + c * ingredients[ingr_list[2]][prop] + d * ingredients[ingr_list[3]][prop]) for prop in range(4))))
  return max_score

def solve(input_file: typing.IO) -> typing.Generator[any, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  ingredients = parse_ingredients(data)
  yield calc_max_score(ingredients, 100)
  yield calc_max_score(ingredients, 100, cals=500)

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
