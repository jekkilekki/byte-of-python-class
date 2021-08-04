# 0805_keyword_args.py

def grades(a = 10, b = 8, c = 6, d = 4, f = 2):
         print('Grades are: A:', a, 'B:', b, 'C:', c, 'D:', d, 'F:', f)

grades()
print('In Korea:')
grades()
print('In America:')
grades(a = 90, b = 80, c = 70, d = 60, f = 50)

print('My grades are:')
grades(a = '3개', f = '0개', c = '1개', b = 0, d = 0)

print('My sister\'s grades are:')
grades(a = '5개', f = '0개')

def grades_real(a = 0, b = 0, c = 0, d = 0, f = 0):
         msg = 'Real grades are: '
         
         if a != 0:
                  msg = msg + 'A:' + str(a) + ', '
         if b != 0:
                  msg = msg + 'B:' + str(b) + ', '
         if c != 0:
                  msg = msg + 'C:' + str(c) + ', '
         if d != 0:
                  msg = msg + 'D:' + str(d) + ', '
         if f != 0:
                  msg = msg + 'F:' + str(f) + ', '
         
         print(msg)

grades_real()
grades_real(a = 3, d = 1)
grades_real(b = 2, c = 2, f = 0)
grades_real(5, 0, 1, 2, 0)

















         
