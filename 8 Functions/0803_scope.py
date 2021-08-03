# 0803_scope.py

x = 50

# Local scope
def local(x):
         print('x is ', x)
         x = 2
         print('x is now ', x)

local(x)
print('x is ', x) 

# global scope
def global_func():
         global x
         
         print('x is ', x)
         x = 2
         print('x is now ', x)

global_func()
print('x is ', x)







         
