import typing

def redistribute(configuration: list):
  """Redistributes the blocks in a memory configuration.

  Arguments:
  configuration -- the memory configuration
  """
  max_blocks = max(configuration)
  max_idx = configuration.index(max_blocks)
  configuration[max_idx] = 0
  for idx in range(len(configuration)):
    configuration[idx] += (max_blocks // len(configuration)) + (1 if 0 < (idx - max_idx) % len(configuration) <= max_blocks % len(configuration) else 0)

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  configuration = [int(blocks) for blocks in input_file.readline().strip().split()]

  seen = {}
  cycles = 0
  while tuple(configuration) not in seen:
    seen[tuple(configuration)] = cycles
    redistribute(configuration)
    cycles += 1

  # PART 1
  yield str(cycles)

  # PART 2
  yield str(cycles - seen[tuple(configuration)])

def main() -> None:
  with open('input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
