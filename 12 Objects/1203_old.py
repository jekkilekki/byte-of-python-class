# 1203_old.py

class Human:
         def __init__(self, name, age = 17):
                  self.name = name
                  self.age = age
                  self.say_hi()

         def say_hi(self):
                  print('\n안녕, 나는 {}살 {}입니다.'.format(self.age, self.name))

         def details(self):
                  print('\n이름: {}\t Age: {}'.format(self.name, self.age), end = '\t')

std = Human('김현우')
me = Human('Aaron', 41)

std.details()
me.details()

# Young Human
class Child(Human):
         def __init__(self, name, age = 10, speed = 5):
                  Human.__init__(self, name, age)
                  self.speed = speed

         def details(self):
                  Human.details(self)
                  print('속도: {}'.format(self.speed))

sister = Child('김수미')
sister.details()

# Old Human
class Adult(Human):
         def __init__(self, name, age = 30, left = 70):
                  Human.__init__(self, name, age)
                  self.left = left

         def details(self):
                  Human.details(self)
                  print('죽을 때까지: {}'.format(self.left))

mom = Adult('김성원')
mom.details()





















