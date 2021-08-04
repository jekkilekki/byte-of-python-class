# 0806_varargs.py

'''VarArgs = Variable number of arguments.
varargs는 가변 개수의 인수에 대한 것입니다.

*params = unlimited single values.
*params는 무제한 단일 값을 위한 것입니다.

**params = unlimited key-value pairs.
**params = 무제한 키-값 쌍.
'''

def gradebook(students = 10, *homework, **grades):
         print('Class gradebook:')
         print('There are', students, 'students in this class.')

         # 튜플의 항목을 반복합니다
         for hw in homework:
                  print('Homework: ', hw)

         # 사전에 있는 항목을 반복합니다
         for hw, grade in grades.items():
                  print(hw, ':', grade)

gradebook()
gradebook(5, 85, 87, 89, 99) # 과제 점수
gradebook(3, 'For loop', 'While loop', 'Functions') # 과제 이름

gradebook(4, hwFor=85, hwWhile=87, hwFun=89) # 과제 점수

gradebook(3, Aaron=85, John=32, Ed=100) # 학생 이름
gradebook(7, 'Chp 1', 'Chp 2', 'Chp 3', hw1=85, hw2=95, hw3 = 79) # 과제 평균 











         
