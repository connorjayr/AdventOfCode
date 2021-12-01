from ..common.intcode import Computer
import itertools
import sys

with open(sys.argv[1], "r") as input_file:
  software = [int(value) for value in input_file.read().split(",")]

# PART 1
permutations = itertools.permutations(range(5))
max_signal = 0
for settings in permutations:
  amplifiers = [Computer(software) for _ in range(5)]
  in_signal = 0
  for i in range(5):
    amplifiers[i].in_values.extend([settings[i], in_signal])
    amplifiers[i].exec_until_pause()
    in_signal = amplifiers[i].out_values[-1]
  max_signal = max(max_signal, in_signal)
print(max_signal)

# PART 2
permutations = itertools.permutations(range(5, 10))
max_signal = 0
for settings in permutations:
  amplifiers = [Computer(software) for _ in range(5)]
  for i in range(5):
    amplifiers[i].in_values.append(settings[i])

  in_signal = 0
  i = 0
  while not amplifiers[-1].halted:
    amplifiers[i].in_values.append(in_signal)
    amplifiers[i].exec_until_pause()
    in_signal = amplifiers[i].out_values[-1]
    i = (i + 1) % len(amplifiers)
  max_signal = max(max_signal, amplifiers[-1].out_values[-1])
print(max_signal)
