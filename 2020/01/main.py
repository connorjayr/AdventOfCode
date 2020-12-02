import typing

def two_sum_product(nums_list: list) -> int:
  """Returns the product of two distinct numbers in a list that add up to 2020.

  Arguments:
  nums_list -- the list of numbers
  """
  nums_set = set(nums_list)
  for _, a in enumerate(nums_list):
    # Look for the complement in the hash set
    if 2020 - a in nums_set:
      return a * (2020 - a)

def three_sum_product(nums_list: list) -> int:
  """Returns the product of three distinct numbers in a list that add up to
  2020.

  Arguments:
  nums_list -- the list of numbers
  """
  nums_set = set(nums_list)
  for i, a in enumerate(nums_list):
    for j, b in enumerate(nums_list):
      # Prevent the same entry from being used twice
      if i == j: continue
      # Look for the complement in the hash set
      if 2020 - a - b in nums_set:
        return a * b * (2020 - a - b)

def solve(input_file: typing.IO) -> typing.Generator[str, None, None]:
  data = [int(line.strip()) for line in input_file]
  yield str(two_sum_product(data))
  yield str(three_sum_product(data))

def main() -> None:
  with open('input.txt', 'r') as input_file:
    for solution in solve(input_file):
      print(solution)

if __name__ == '__main__':
  main()
