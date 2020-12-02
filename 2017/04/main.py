import typing

def is_valid_passphrase(passphrase: str) -> bool:
  """Returns true iff the given passphrase is valid; i.e., it is made up of
  unique words.

  Arguments:
  passphrase -- the passphrase
  """
  passwords = passphrase.split()
  return len(passwords) == len(set(passwords))

def is_valid_secure_passphrase(passphrase: str) -> bool:
  """Returns true iff the given passphrase is valid using the new security
  policy; i.e., it is made up of unique words which are not anagrams of each
  other.

  Arguments:
  passphrase -- the passphrase
  """
  passwords = [''.join(sorted(password)) for password in passphrase.split()]
  return len(passwords) == len(set(passwords))

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  passphrases = [passphrase.strip() for passphrase in input_file if passphrase.strip()]

  # PART 1
  yield str([is_valid_passphrase(passphrase) for passphrase in passphrases].count(True))

  # PART 2
  yield str([is_valid_secure_passphrase(passphrase) for passphrase in passphrases].count(True))


def main() -> None:
  with open('input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
