import typing

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  spreadsheet = [[int(cell) for cell in row.split()] for row in input_file]

  # PART 1
  yield sum([max(row) - min(row) for row in spreadsheet])

  # PART 2
  checksum = 0
  for row in spreadsheet:
    for i in range(len(row)):
      for j in range(len(row)):
        if i == j: continue
        if row[i] % row[j] == 0:
          checksum += row[i] // row[j]
  yield str(checksum)

def main() -> None:
  with open('input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
