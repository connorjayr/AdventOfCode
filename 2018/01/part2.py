import sys

changes = []
with open(sys.argv[1], "r") as input_file:
  for line in input_file.readlines():
    changes.append(int(line))

reached = set()
frequency = 0
i = 0
while frequency not in reached:
  reached.add(frequency)
  frequency += changes[i]

  i = (i + 1) % len(changes)

print(frequency)