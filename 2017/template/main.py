import typing

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  yield 'Solution not implemented'

def main() -> None:
  with open('input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
