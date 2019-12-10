import math
import sys

WIDTH = 25
HEIGHT = 6
LAYER_LENGTH = WIDTH * HEIGHT

def print_image(image: list):
  for row in range(HEIGHT):
    for col in range(WIDTH):
      print("█" if image[row * WIDTH + col] == "1" else " ", end="")
    print()

layers = []
with open(sys.argv[1], "r") as input_file:
  data = input_file.read().strip()
  i = 0
  while i < len(data):
    layers.append(data[i:i + LAYER_LENGTH])
    i += LAYER_LENGTH

layer = min(layers, key=lambda layer: layer.count("0"))
print(layer.count("1") * layer.count("2"))

image = layers[0]
for layer in layers:
  for i in range(LAYER_LENGTH):
    if image[i] == "2":
      image = image[:i] + layer[i] + image[i + 1:]

print_image(image)