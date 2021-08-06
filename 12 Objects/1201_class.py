# 1201_class.py

class Person:
         def __init__(self, name):
                  self.name = name
         
         def say_hi(self):
                  print('Hello, my name is {}!'.format(self.name))

p = Person('Aaron')
p.say_hi()
