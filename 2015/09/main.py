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

def parse_cities(lines: list) -> dict:
  """Parses a list of lines from the input file into distances between cities.

  Arguments:
  lines -- the lines of input
  """
  cities = collections.defaultdict(list)
  for line in lines:
    tokens = line.split()
    # Bidirectional edge
    cities[tokens[0]].append((tokens[2], int(tokens[4])))
    cities[tokens[2]].append((tokens[0], int(tokens[4])))
  return cities

def visit_all(start: str, cities: dict, visited: set, find_shortest_path: bool) -> int:
  """Returns the minimum distance needed to visit every city starting at a given
  city.

  Arguments:
  start -- the starting city
  cities -- maps cities to pairs of other cities and the distance between them
  visited -- tracks which cities have been visited so far
  find_shortest_path -- true if the find_shortest_path path should be found,
  false if the longest path should be found
  """
  # If we have visited every city, then no more distance is required to visit
  # every city
  if len(visited) == len(cities): return 0

  dist = math.inf if find_shortest_path else -math.inf
  for neighbor in cities[start]:
    # Skip cities which we have already visited
    if neighbor[0] in visited: continue
    # Use backtracking to generate all paths
    visited.add(neighbor[0])
    if find_shortest_path:
      dist = min(dist, neighbor[1] + visit_all(neighbor[0], cities, visited, find_shortest_path))
    else:
      dist = max(dist, neighbor[1] + visit_all(neighbor[0], cities, visited, find_shortest_path))
    visited.remove(neighbor[0])
  return dist

def traveling_salesman_dist(cities: dict, find_shortest_path: bool) -> int:
  """Returns the total distance traveled when solving the traveling salesman
  problem; i.e., each city is visited once.

  Arguments:
  cities -- maps cities to pairs of other cities and the distance between them
  find_shortest_path -- true if the find_shortest_path path should be found,
  false if the longest path should be found
  """
  dist = math.inf if find_shortest_path else -math.inf
  for start in cities:
    visited = set([start])
    if find_shortest_path:
      dist = min(dist, visit_all(start, cities, visited, find_shortest_path))
    else:
      dist = max(dist, visit_all(start, cities, visited, find_shortest_path))
  return dist

def solve(input_file: typing.IO) -> typing.Generator[any, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  cities = parse_cities(data)
  yield traveling_salesman_dist(cities, True)
  yield traveling_salesman_dist(cities, False)

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
