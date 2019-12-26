from ..common.intcode import Computer
import sys

with open(sys.argv[1], "r") as input_file:
  intcode = [int(value) for value in input_file.read().split(",")]

# PART 1
network = [Computer(intcode) for _ in range(50)]
for i in range(len(network)):
  network[i].in_values.append(i)

first = None
prev = set()
nat = [-1]
while True:
  for computer in network:
    computer.exec_until_pause()
    for i in range(0, len(computer.out_values), 3):
      address = computer.out_values[i]
      packet = computer.out_values[i + 1:i + 3]
      if address == 255:
        if first is None:
          first = packet[1]
        nat = packet
      if address < len(network):
        network[address].in_values.extend(packet)
    computer.out_values.clear()

  idle = True
  for computer in network:
    if len(computer.in_values) == 0:
      computer.in_values.append(-1)
    else:
      idle = False

  if idle:
    if tuple(nat) in prev:
      print(first)
      print(nat[1])
      exit(0)
    prev.add(tuple(nat))

    network[0].in_values = list(nat)