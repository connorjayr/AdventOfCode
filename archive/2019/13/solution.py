from ..common.intcode import Computer
import sys

def parse_grid(computer: Computer, grid: dict) -> tuple:
  paddle = (0, 0)
  ball = (0, 0)
  for i in range(0, len(computer.out_values), 3):
    x = computer.out_values[i]
    y = computer.out_values[i + 1]
    tile_id = computer.out_values[i + 2]
    grid[(x, y)] = tile_id

    if tile_id == 3:
      paddle = (x, y)
    elif tile_id == 4:
      ball = (x, y)
  computer.out_values.clear()
  return paddle, ball

with open(sys.argv[1], "r") as input_file:
  intcode = [int(value) for value in input_file.read().split(",")]

# PART 1
computer = Computer(intcode)
grid = {}

computer.exec_until_pause()
parse_grid(computer, grid)
print(list(grid.values()).count(2))

# PART 2
computer = Computer(intcode)
computer.intcode[0] = 2
grid = {}

ball = (0, 0)
paddle = (0, 0)
while not computer.halted:
  computer.exec_until_pause()
  paddle, ball = parse_grid(computer, grid)

  if paddle[0] < ball[0]:
    computer.in_values.append(1)
  elif paddle[0] > ball[0]:
    computer.in_values.append(-1)
  else:
    computer.in_values.append(0)
print(grid[(-1, 0)])