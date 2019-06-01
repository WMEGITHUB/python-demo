c = 50

def add(x, y):
  c = x + y
  print(c)

add(1, 2)
print(c)


def funcdemo():
  global ff
  ff = 2

funcdemo()
print(ff)