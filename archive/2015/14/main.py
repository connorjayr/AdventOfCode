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

def parse_reindeer(lines: list) -> dict:
  """Parses the speed, flying time, and resting time for each reindeer.

  Arguments:
  lines -- the lines of input
  """
  reindeer = {}
  for line in lines:
    tokens = line.split()
    reindeer[tokens[0]] = (int(tokens[3]), int(tokens[6]), int(tokens[-2]))
  return reindeer

def calc_distance_after(reindeer: tuple, time: int) -> int:
  """Returns the distance that the given reindeer has traveled after a certain
  amount of time.

  Arguments:
  reindeer -- a 3-tuple containing the speed, flying time, and resting time of
  the given reindeer
  time -- the total time
  """
  period = reindeer[1] + reindeer[2]
  return (time // period) * reindeer[0] * reindeer[1] + reindeer[0] * min(time % period, reindeer[1])

def calc_max_points(reindeer: dict, time: int) -> int:
  """Calculates the number of points that the winning reindeer has after a
  certain amount of time.

  Arguments:
  reindeer -- maps reindeer to a 3-tuple containing their speed, flying time,
  and resting time
  time -- the total time
  """
  dist = collections.defaultdict(int)
  points = collections.defaultdict(int)
  for t in range(time):
    for name, r in reindeer.items():
      period = r[1] + r[2]
      if t % period < r[1]:
        dist[name] += r[0]
    points[max((r for r in dist.items()), key=lambda r : r[1])[0]] += 1
  return max(points.values())

def solve(input_file: typing.IO) -> typing.Generator[any, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  reindeer = parse_reindeer(data)
  yield max(calc_distance_after(r, 2503) for r in reindeer.values())
  yield calc_max_points(reindeer, 2503)

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
