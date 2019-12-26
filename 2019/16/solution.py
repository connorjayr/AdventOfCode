import itertools
import sys

def get_pattern(i: int) -> iter:
  return itertools.cycle([0] * i + [1] * i + [0] * i + [-1] * i)

with open(sys.argv[1], "r") as input_file:
  number = [int(digit) for digit in input_file.read().strip()]

# PART 1
prev = list(number)
for phase in range(100):
  curr = [0] * len(prev)
  for i in range(len(prev)):
    pattern = get_pattern(i + 1)
    next(pattern)

    for digit in prev:
      curr[i] += next(pattern) * digit
  for i in range(len(curr)):
    digit = str(curr[i])
    if len(digit) > 1:
      curr[i] = int(digit[-1])
  prev = curr
print("".join([str(digit) for digit in prev])[:8])

# PART 2
number = list(number) * 10000
offset = sum([10 ** (6 - i) * number[i] for i in range(7)])
number = number[offset:]
for phase in range(100):
  digit_sum = 0
  for i in range(len(number) - 1, -1, -1):
    digit_sum = (digit_sum + number[i]) % 10
    number[i] = digit_sum
print("".join([str(digit) for digit in number])[:8])