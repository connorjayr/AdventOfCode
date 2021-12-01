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

def rotate_ccw(pos, deg):
  """Rotates a point counter-clockwise about the origin.

  Arguments:
  pos -- the original position
  deg -- the number of degrees to rotate; must be a multiple of 90
  """
  for _ in range((deg // 90) % 4):
    pos = (-pos[1], pos[0])
  return pos

def navigate_ship(instructions: list) -> int:
  """Navigates a ship using given instructions. Returns the manhattan distance
  between the final position and the starting position.

  Arguments:
  instructions -- the movement instructions
  """
  ship = (0, 0)
  dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
  dir_idx = 0
  for instruction in instructions:
    action = instruction[0]
    arg = int(instruction[1:])
    if action == 'N':
      ship = (ship[0], ship[1] + arg)
    elif action == 'E':
      ship = (ship[0] + arg, ship[1])
    elif action == 'S':
      ship = (ship[0], ship[1] - arg)
    elif action == 'W':
      ship = (ship[0] - arg, ship[1])
    elif action == 'L':
      dir_idx = (dir_idx + arg // 90) % len(dirs)
    elif action == 'R':
      dir_idx = (dir_idx - arg // 90) % len(dirs)
    elif action == 'F':
      ship = (ship[0] + dirs[dir_idx][0] * arg, ship[1] + dirs[dir_idx][1] * arg)
  return abs(ship[0]) + abs(ship[1])

def navigate_ship_with_waypoint(instructions: list) -> int:
  """Navigates a ship and waypoint using given instructions. Returns the
  manhattan distance between the final position of the ship and its starting
  position.

  Arguments:
  instructions -- the movement instructions
  """
  ship = (0, 0)
  waypt = (10, 1)
  for instruction in instructions:
    action = instruction[0]
    arg = int(instruction[1:])
    if action == 'N':
      waypt = (waypt[0], waypt[1] + arg)
    elif action == 'E':
      waypt = (waypt[0] + arg, waypt[1])
    elif action == 'S':
      waypt = (waypt[0], waypt[1] - arg)
    elif action == 'W':
      waypt = (waypt[0] - arg, waypt[1])
    elif action == 'L':
      waypt = rotate_ccw(waypt, arg)
    elif action == 'R':
      waypt = rotate_ccw(waypt, 360 - arg)
    elif action == 'F':
      ship = (ship[0] + waypt[0] * arg, ship[1] + waypt[1] * arg)
  return abs(ship[0]) + abs(ship[1])

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [parse_line(line.strip()) for line in input_file if line.strip()]
  yield str(navigate_ship(data))
  yield str(navigate_ship_with_waypoint(data))

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
