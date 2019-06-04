f = lambda x, y: x + y

print(f(1, 2))

x = 2
y = 3
r = x if x < y else y

print(r)

demo = [1, 2, 3]
def demoFunc(x):
  return x * x

hh = map(demoFunc, demo)
print(list(hh))