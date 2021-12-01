import sys

counts = [0, 0]
with open(sys.argv[1], "r") as input_file:
  for box_id in input_file.readlines():
    freq = {}
    for char in box_id:
      freq[char] = freq.get(char, 0) + 1

    if 2 in freq.values(): counts[0] += 1
    if 3 in freq.values(): counts[1] += 1

print(counts[0] * counts[1])