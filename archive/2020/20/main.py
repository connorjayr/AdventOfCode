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

def rotate_and_flip(tile: list) -> list:
  variations = [list(tile), [row[::-1] for row in tile]]
  for _ in range(3):
    rotated_tile = [''.join(row) for row in zip(*tile[::-1])]
    tile = rotated_tile
    variations.extend([list(tile), [row[::-1] for row in tile]])
  return variations

def index_borders(tiles, borders):
  for tile_num, variations in tiles.items():
    for tile_idx, tile in enumerate(variations):
      borders['top'][tile[0]].add((tile_num, tile_idx))
      borders['bottom'][tile[9]].add((tile_num, tile_idx))
      borders['left'][''.join([row[0] for row in tile])].add((tile_num, tile_idx))
      borders['right'][''.join([row[9] for row in tile])].add((tile_num, tile_idx))

def find_sea_monsters(tiles, image):
  composite = []
  for row_offset in range(12):
    tile_row = image[row_offset * 12:(row_offset + 1) * 12]
    for row_num in range(1, 9):
      composite.append(''.join([tiles[tile[0]][tile[1]][row_num][1:9] for tile in tile_row]))
  monster = [(0, 1), (1, 2), (4, 2), (5, 1), (6, 1), (7, 2), (10, 2), (11, 1), (12, 1), (13, 2), (16, 2), (17, 1), (18, 0), (18, 1), (19, 1)]
  monsters = 0
  for y in range(96 - 3):
    for x in range(96 - 20):
      if all([composite[y + offset[1]][x + offset[0]] == '#' for offset in monster]):
        monsters += 1
  print(sum([row.count('#') for row in composite]) - monsters * 15)

def recurse(tiles, image, used, borders):
  if len(image) == 144:
    print(functools.reduce(lambda a, b : a * b, [image[0][0], image[11][0], image[132][0], image[143][0]]))
    find_sea_monsters(tiles, image)
    return
  poss = set([(tile_num, tile_idx) for tile_num in tiles.keys() for tile_idx in range(len(tiles[tile_num]))])
  if len(image) >= 12:
    poss.intersection_update(set([el for el in borders['top'][tiles[image[-12][0]][image[-12][1]][9]] if el[0] not in used]))
  if len(image) % 12 > 0:
    poss.intersection_update(set([el for el in borders['left'][''.join([row[9] for row in tiles[image[-1][0]][image[-1][1]]])] if el[0] not in used]))
  for el in poss:
    image.append(el)
    used.add(el[0])
    recurse(tiles, image, used, borders)
    used.remove(el[0])
    image.pop()

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  # data = [parse_line(line.strip()) for line in input_file if line.strip()]
  data = split_into_groups([line.strip() for line in input_file])
  tiles = {}
  for tile in data:
    tile_num = int(tile[0][5:-1])
    tiles[tile_num] = rotate_and_flip(tile[1:])
  borders = {'top': collections.defaultdict(set), 'left': collections.defaultdict(set), 'right': collections.defaultdict(set), 'bottom': collections.defaultdict(set)}
  index_borders(tiles, borders)

  print(len(tiles))
  image = []
  used = set()
  recurse(tiles, image, used, borders)

def main() -> None:
  """Called when the script is run."""
  with open(f'{os.path.dirname(__file__)}/input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()

''.join(['a', 'b']) ==> 'ab'
