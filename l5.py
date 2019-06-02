class Student():
  name = 'wang'
  age = 22
  sum = 0

  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.__score = 0
    self.plus_sum()
  
  def marking(self, score):
    self.__score = score
    print('score: ' + str(self.__score))

  @classmethod
  def plus_sum(cls):
    cls.sum += 1

  @staticmethod
  def add(x, y):
    return x + y

student1 = Student('li', 18)
student1.marking(59)