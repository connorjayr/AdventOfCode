import typing

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  sequence = input_file.readline().strip()

  # PART 1
  digit_sum = 0
  for i in range(len(sequence)):
    if sequence[i] == sequence[(i + 1) % len(sequence)]:
      digit_sum += int(sequence[i])
  yield str(digit_sum)

  # PART 2
  digit_sum = 0
  for i in range(len(sequence)):
    if sequence[i] == sequence[(i + len(sequence) // 2) % len(sequence)]:
      digit_sum += int(sequence[i])
  yield str(digit_sum)

def main() -> None:
  with open('input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
