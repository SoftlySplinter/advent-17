from captcha import solve, solve2


def test_example1():
  assert solve('1122') == 3

def test_example2():
  assert solve('1111') == 4

def test_example3():
  assert solve('1234') == 0

def test_example4():
  assert solve('91212129') == 9

def test2_example1():
  assert 6 == solve2('1212')

def test2_example2():
  assert 0 == solve2('1221')

def test2_example3():
  assert 4 == solve2('123425')

def test2_example4():
  assert 12 == solve2('123123')

def test2_example5():
  assert 4 == solve2('12131415')
