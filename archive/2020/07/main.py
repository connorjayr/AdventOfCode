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

def build_graph(rules: list) -> nx.DiGraph:
  """Builds a graph describing bag relationships from a list of rules.

  Arguments:
  rules -- the list of rules; e.g. "a b bags contain 1 c d bag, 2 e f bags."
  """
  G = nx.DiGraph()
  for rule in rules:
    bag, contains = list(re.match(r'(.+) bags contain (.+).', rule).groups())
    G.add_node(bag)
    if contains != 'no other bags':
      for contained in contains.split(', '):
        amnt, child = list(re.match(r'(\d+) (.+) bags?', contained).groups())
        G.add_edge(bag, child, amount=int(amnt))
  return G

def count_contained_bags(G: nx.DiGraph, bag: str) -> int:
  """Counts the total number of bags that a bag contains.

  Arguments:
  bag -- the name of the original bag
  """
  return sum([attr['amount'] * (1 + count_contained_bags(G, child)) for child, attr in G[bag].items()])

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  G = build_graph(data)
  yield str(['shiny gold' in nx.algorithms.dag.descendants(G, bag) for bag in G.nodes() if bag != 'shiny gold'].count(True))
  yield str(count_contained_bags(G, 'shiny gold'))

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
