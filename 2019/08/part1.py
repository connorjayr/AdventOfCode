import math
import sys

layers = []
with open(sys.argv[1], "r") as input_file:
  data = input_file.read().strip()
  i = 0
  while i < len(data):
    layers.append(data[i:i + 150])
    i += 150

min_layer = None
min_count = math.inf
for layer in layers:
  count = layer.count("0")
  if count < min_count:
    min_layer = layer
    min_count = count
print(min_layer.count("1") * min_layer.count("2"))

image = layers[0]
for layer in layers:
  for i in range(150):
    if image[i] == "2":
      image = image[:i] + layer[i] + image[i + 1:]
i = 0
while i < len(image):
  row = image[i:i + 25]
  for c in row:
    if c == "0":
      print(" ", end="")
    else:
      print("O", end="")
  print()
  i += 25