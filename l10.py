import time

def decorate(func):
  def wrapper(*args, **kw):
    print(time.time())
    func(*args, **kw)
  return wrapper


@decorate
def f1(funcname1, funcname2, **kw):
  print('this is a function' + funcname1)
  print('this is a function' + funcname2)
  print(kw)

f1('test1', 'test2', a=1, b=2, c=3)