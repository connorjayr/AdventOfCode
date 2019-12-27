from ..common.intcode import Computer
import itertools
import sys

items = [
  "planetoid",
  "spool of cat6",
  "dark matter",
  "sand",
  "coin",
  "wreath",
  "fuel cell",
  "jam",
]

def run_brute_force(computer: Computer):
  for n in range(len(items) + 1):
    for inv in itertools.combinations(items, n):
      for item in inv:
        computer.in_values.extend([ord(c) for c in f"take {item}\n"])
      computer.exec_until_pause()
      computer.out_values.clear()
      
      computer.in_values.extend([ord(c) for c in "south\n"])
      computer.exec_until_pause()
      out_str = "".join([chr(i) for i in computer.out_values])
      if "lighter" not in out_str and "heavier" not in out_str:
        print(inv)
        print("".join([chr(i) for i in computer.out_values]))
        computer.out_values.clear()
        return
      else:
        for item in inv:
          computer.in_values.extend([ord(c) for c in f"drop {item}\n"])

with open(sys.argv[1], "r") as input_file:
  intcode = [int(value) for value in input_file.read().split(",")]
computer = Computer(intcode)

while not computer.halted:
  computer.exec_until_pause()
  print("".join([chr(i) for i in computer.out_values]))
  computer.out_values.clear()

  if not computer.halted:
    input_str = input() + "\n"

    if input_str == "brute_force\n":
      run_brute_force(computer)

    computer.in_values.extend([ord(c) for c in input_str])