from l6 import Human

class Teacher(Human):
  def __init__(self, school, name):
    self.school = school
    super(Teacher, self).__init__(name)

  def teaching(self):
    print('teaching...' + self.school)
    super(Teacher, self).humanName()

teacher1 = Teacher('primary school', 'teacher1')
teacher1.humanName()
teacher1.teaching()