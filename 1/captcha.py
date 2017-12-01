import sys
from functools import reduce 

def solve(captcha):
  digits = [ int(digit) for digit in captcha ]
  digits_offset = digits[1:] + digits[:1]

  pair_values = [ value for value, offset in zip(digits, digits_offset) if value == offset] 

  return sum(pair_values)

def solve2(captcha):
  digits = [ int(digit) for digit in captcha ]
  lengths = len(digits)
  digits_offset = digits[int(lengths/2):] + digits[:int(lengths/2)]

  print(digits_offset)
  

  pair_values = [ value for value, offset in zip(digits, digits_offset) if value == offset] 

  return sum(pair_values)


def get_pair_value(pair):
  x, y = pair

  if(x == y):
    return x
  return 0

if __name__ == '__main__': 
  print(solve2(sys.argv[1]))
