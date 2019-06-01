# def function
def funcname(a, b=5) :
  return a/b

a = funcname(a=5)
print(a)

def hhhdemo(**parameter_list):
  for key, value in parameter_list.items():
    print(key, value)

c = {'c': 1, 'd': 2}
hhhdemo(**c)