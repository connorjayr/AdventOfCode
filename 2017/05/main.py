import typing

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  og_instructions = [int(offset.strip()) for offset in input_file if offset]

  # PART 1
  instructions = list(og_instructions)
  idx = 0
  steps = 0
  while 0 <= idx < len(instructions):
    next_idx = idx + instructions[idx]
    instructions[idx] += 1
    idx = next_idx
    steps += 1
  yield str(steps)

  # PART 2
  instructions = list(og_instructions)
  idx = 0
  steps = 0
  while 0 <= idx < len(instructions):
    next_idx = idx + instructions[idx]
    instructions[idx] += (1 if instructions[idx] < 3 else -1)
    idx = next_idx
    steps += 1
  yield str(steps)

def main() -> None:
  with open('input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
