import sys

frequency = 0
with open(sys.argv[1], "r") as input_file:
  for line in input_file.readlines():
    frequency += int(line)

print(frequency)