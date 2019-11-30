import sys

def is_pair(a, b):
  if len(a) != len(b): return False

  for i in range(len(a)):
    if a[:i] + a[i + 1:] == b[:i] + b[i + 1:]:
      print(a[:i] + a[i + 1:])
      return True

box_ids = []
with open(sys.argv[1], "r") as input_file:
  for box_id in input_file.readlines():
    box_ids.append(box_id)

for i in range(len(box_ids)):
  for j in range(len(box_ids)):
    if i == j: continue

    if is_pair(box_ids[i], box_ids[j]):
      exit(0)