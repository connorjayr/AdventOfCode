import collections
import functools
import itertools
import operator
import re
import typing

def bin_search(instructions: str) -> int:
  """Performs a binary search between 0 and 2^l - 1, where l is the number of
  instructions (take upper or lower).

  Arguments:
  instructions -- a list of instructions which tell which half to take; True if
  upper, false otherwise
  """
  low = 0
  high = (2 ** len(instructions)) - 1
  for upper in instructions:
    mid = (low + high + 1) // 2
    if upper:
      low = mid
    else:
      high = mid - 1
  return low

def decode_seat_id(boarding_pass: str) -> int:
  """Calculates a seat id from a boarding pass string.

  Arguments:
  boarding_pass -- a 10-character boarding pass
  """
  row = bin_search([letter == 'B' for letter in boarding_pass[:7]])
  col = bin_search([letter == 'R' for letter in boarding_pass[7:10]])
  return row * 8 + col

def find_missing_seat(seat_ids: list) -> int:
  """Finds the missing seat id in a block of consecutive seat ids.

  Arguments:
  seat_ids -- a list of consecutive seat ids
  """
  seat_ids = set(seat_ids)
  for seat_id in range(min(seat_ids) + 1, max(seat_ids)):
    if seat_id not in seat_ids and seat_id - 1 in seat_ids and seat_id + 1 in seat_ids:
      return seat_id

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  data = [line.strip() for line in input_file if line]
  seat_ids = [decode_seat_id(boarding_pass) for boarding_pass in data]
  yield str(max(seat_ids))
  yield str(find_missing_seat(seat_ids))

def main() -> None:
  with open('input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
