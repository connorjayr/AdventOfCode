import typing

def is_valid_with_old_policy(line: str) -> bool:
  """Returns true iff a password is valid using the old password policy; i.e.,
  the first part of the line describes how many occurrences of a particular
  character are allowed.

  Arguments:
  line -- the line of input
  """
  policy, passwd = line.split(': ')
  occurrences_range, char = policy.split()
  min_occurrences, max_occurrences = [int(n) for n in occurrences_range.split('-')]
  return min_occurrences <= passwd.count(char) <= max_occurrences

def is_valid_with_new_policy(line: str) -> bool:
  """Returns true iff a password is valid using the new password policy; i.e.,
  the first part of the line describes which characters should occur at the
  two positions.

  Arguments:
  line -- the line of input
  """
  policy, passwd = line.split(': ')
  positions, char = policy.split()
  # Adjust from one-indexing to zero-indexing
  positions = [int(i) - 1 for i in positions.split('-')]
  # Search for positional matches in the password
  matches = [passwd[pos] == char for pos in positions]
  return any(matches) and not all(matches)

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  data = [line.strip() for line in input_file if line]
  yield str([is_valid_with_old_policy(line) for line in data].count(True))
  yield str([is_valid_with_new_policy(line) for line in data].count(True))
  
def main() -> None:
  with open('input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
