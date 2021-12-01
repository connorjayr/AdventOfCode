import sys

# credit to Mart Bakhoff (https://stackoverflow.com/a/9758173)
def egcd(a, b):
  if a == 0:
    return (b, 0, 1)
  else:
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
  g, x, y = egcd(a, m)
  if g != 1:
    raise Exception("Modular inverse does not exist")
  else:
    return x % m

def deal_into_new_stack(i: int, N: int) -> int:
  return N - i - 1

def inv_deal_into_new_stack(i: int, N: int) -> int:
  return deal_into_new_stack(i, N)

def cut(i: int, j: int, N: int) -> int:
  return (i - j) % N

def inv_cut(i: int, j: int, N: int) -> int:
  return (i + j) % N

def deal_with_increment(i: int, j: int, N: int) -> int:
  return (i * j) % N

def inv_deal_with_increment(i: int, j: int, N: int) -> int:
  return (modinv(j, N) * i) % N

def inv(i: int, N: int) -> int:
  with open(sys.argv[1], "r") as input_file:
    inv_methods = input_file.readlines()
    inv_methods.reverse()
    for method in inv_methods:
      method = method.strip()
      if method == "deal into new stack":
        i = inv_deal_into_new_stack(i, N)
      elif method.startswith("cut"):
        i = inv_cut(i, int(method.split()[-1]), N)
      elif method.startswith("deal with increment"):
        i = inv_deal_with_increment(i, int(method.split()[-1]), N)
  return i

# PART 1
i = 2019
N = 10007
with open(sys.argv[1], "r") as input_file:
  for method in input_file:
    method = method.strip()
    if method == "deal into new stack":
      i = deal_into_new_stack(i, N)
    elif method.startswith("cut"):
      i = cut(i, int(method.split()[-1]), N)
    elif method.startswith("deal with increment"):
      i = deal_with_increment(i, int(method.split()[-1]), N)
print(i)

# PART 2
i = 2020
N = 119315717514047
j = inv(i, N)
k = inv(j, N)

# credit to /u/etotheipi1 (https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbnifwk?utm_source=share&utm_medium=web2x)
a = (j - k) * modinv(i - j + N, N) % N
b = (j - a * i) % N

repeat = 101741582076661
print((pow(a, repeat, N) * i + (pow(a, repeat, N) - 1) * modinv(a - 1, N) * b) % N)