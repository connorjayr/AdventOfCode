import sys

requirements = []
with open(sys.argv[1], "r") as input_file:
  requirements = [int(n) for n in input_file.readlines()]

print(sum([n // 3 - 2 for n in requirements]))