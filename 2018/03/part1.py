import sys

SIDE_LENGTH = 1000

def add_claim(fabric, claim):
  claim = claim.strip().split()
  
  claim_id = int(claim[0][1:])
  top_left = [int(n) for n in claim[2][:-1].split(",")]
  dimensions = [int(n) for n in claim[3].split("x")]
  for row in range(top_left[1], top_left[1] + dimensions[1]):
    for col in range(top_left[0], top_left[0] + dimensions[0]):
      fabric[row][col].append(claim_id)

fabric = [[[] for col in range(SIDE_LENGTH)] for row in range(SIDE_LENGTH)]
with open(sys.argv[1], "r") as input_file:
  for claim in input_file.readlines():
    add_claim(fabric, claim)

overlap = 0
for row in range(SIDE_LENGTH):
  for col in range(SIDE_LENGTH):
    if len(fabric[row][col]) > 1:
      overlap += 1

print(overlap)