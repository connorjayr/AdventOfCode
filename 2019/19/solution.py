from ..common.intcode import Computer
import sys

with open(sys.argv[1], "r") as input_file:
  intcode = [int(value) for value in input_file.read().split(",")]

def is_in_beam(point: tuple) -> bool:
  computer = Computer(intcode)
  computer.in_values.extend([point[0], point[1]])
  computer.exec_until_pause()
  return computer.out_values[-1] == 1

# PART 1
count = 0
for x in range(50):
  for y in range(50):
    count += is_in_beam((x, y))
print(count)

# PART 2
x = 0
y = 99
while not is_in_beam((x + 99, y - 99)):
  y += 1
  while not is_in_beam((x, y)):
    x += 1
print(x * 10000 + y - 99)