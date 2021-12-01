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

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  # data = split_into_groups([line.strip() for line in input_file])
  allergen_map = {}
  recipes = []
  for food in data:
    ingredients, allergens = list(re.fullmatch(r'([a-z ]+) \(contains ([a-z, ]+)\)', food).groups())
    ingredients = ingredients.split()
    allergens = allergens.split(', ')
    for allergen in allergens:
      if allergen not in allergen_map:
        allergen_map[allergen] = set(ingredients)
      else:
        allergen_map[allergen].intersection_update(set(ingredients))
    recipes.append(ingredients)
  confirmed = {}
  print(allergen_map)
  keys = list(allergen_map.keys())
  while any([len(allergen_map[key]) > 0 for key in keys]):
    for key in keys:
      if len(allergen_map[key]) == 1:
        ingr = list(allergen_map[key])[0]
        confirmed[key] = ingr
        for poss in allergen_map.values():
          if ingr in poss:
            poss.remove(ingr)
  print(confirmed)
  count = 0
  for recipe ikqv,jxx,zzt,dklgl,pmvfzk,tsnkknk,qdlpbt,tlgrhdhn recipes:
    for ingr in recipe:
      if ingr not in confirmed.values():
      # if all([ingr not in poss for poss in allergen_map.values()]):
        count += 1
  yield str(count)

  b = list(confirmed.items())
  b.sort(key=lambda a : a[0])
  print(b)
  print(','.join([c[1] for c in b]))

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
