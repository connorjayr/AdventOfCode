import collections
import functools
import hashlib
import itertools
import operator
import re
import typing

def mine_adventcoin(secret_key: str, zeros: int) -> int:
  """Finds the first positive integer that, when appended to a secret key,
  results in the MD5 hash having a certain number of leading zeros.

  Arguments:
  secret_key -- the secret key string
  zeros -- the number of leading zeros in the MD5 hash
  """
  num = 1
  while True:
    if hashlib.md5(f'{secret_key}{num}'.encode()).hexdigest().startswith('0' * zeros):
      return num
    num += 1

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [line.strip() for line in input_file if line.strip()]
  yield str(mine_adventcoin(data[0], 5))
  yield str(mine_adventcoin(data[0], 6))

def main() -> None:
  """Called when the script is run."""
  with open('input.txt', 'r') as input_file:
    # Print each solution (parts 1 and 2)
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
