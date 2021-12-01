import collections
import functools
import itertools
import operator
import re
import sys
import typing

def escape_characters(string: str) -> str:
  """Converts a string in code to a string in memory. Escape sequences are
  converted to an appropriate character, except for hexadecimal characters
  (which are replaced with a '?').

  Arguments:
  string -- the string representation in code
  """
  escaped_str = ''
  # Use idx to iterate over the string in code to avoid "chain reaction"
  # conversions; e.g. "\\x00" -> "\x00" -> '?'
  idx = 1
  while idx + 1 < len(string):
    # Check for an escape sequence
    if string[idx] == '\\':
      # In each of the following cases, increment idx by the appropriate amount
      # to advance to the next character not included in this escape sequence
      if string[idx + 1] == '\\':
        escaped_str += '\\'
        idx += 2
      elif string[idx + 1] == '"':
        escaped_str += '"'
        idx += 2
      elif re.match(r'x[\da-f]{2}', string[idx + 1:idx + 4]):
        escaped_str += '?'
        idx += 4
      else:
        print('ERROR: Invalid escape sequence', file=sys.stderr)
        exit(1)
    else:
      escaped_str += string[idx]
      idx += 1
  return escaped_str

def encode_characters(string: str) -> str:
  """Converts a string in memory to a string in code.

  Arguments:
  string -- the string representation in code
  """
  # Do the backslash replacement first to avoid the following:
  # '"' -> '\"' -> '\\"'
  return '"' + string.replace('\\', '\\\\').replace('"', '\\"') + '"'

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  """Generates solutions to the problem.

  Arguments:
  input_file -- the file containing the input
  """
  data = [line.strip() for line in input_file if line.strip()]
  yield str(sum([len(string) for string in data]) - sum([len(escape_characters(string)) for string in data]))
  yield str(sum([len(encode_characters(string)) for string in data]) - sum([len(string) for string in data]))

def main() -> None:
  """Called when the script is run."""
  with open('input.txt', 'r') as input_file:
    # Print each solution (parts 1 and 2)
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
