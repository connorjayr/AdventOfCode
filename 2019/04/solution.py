import sys

def get_digits(n: int) -> list:
  digits = []
  while n > 0:
    digits.append(n % 10)
    n //= 10
  digits.reverse()
  return digits

def get_digit_frequencies(n: int) -> dict:
  freq = {}
  for digit in get_digits(n):
    freq[digit] = freq.get(digit, 0) + 1
  return freq

def is_ascending(n: int) -> bool:
  digits = get_digits(n)
  for i in range(len(digits) - 1):
    if digits[i] > digits[i + 1]:
      return False
  return True

min_pass = 125730
max_pass = 579381

# PART 1
print(sum([is_ascending(password) and any([freq >= 2 for freq in get_digit_frequencies(password).values()]) for password in range(min_pass, max_pass + 1)]))
# PART 2
print(sum([is_ascending(password) and 2 in get_digit_frequencies(password).values() for password in range(min_pass, max_pass + 1)]))