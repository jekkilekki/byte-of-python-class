# 0807_return.py

def average(*grades):
         '''Function: average(*grades).
학생 성적의 평균을 구합니다'''
         total = 0
         
         for grade in grades:
                  total += grade

         return total / len(grades)

print('Average of grades: ', average(90, 100)) # 95
print('My grade: ', average(75, 77, 95, 100, 100, 88, 89, 83, 95))


def letter_grade(num):
         '''Function: letter_grade(num).
평균을 기반으로 학생의 문자 등급을 찾습니다.
(A, B, C, D, F)

A >= 90
B >= 80
C >= 70
D >= 60
F < 60
'''
         # A >= 90
         if num >= 90:
                  return 'A'

         # B >= 80
         elif num >= 80:
                  return 'B'

         # C >= 70
         elif num >= 70:
                  return 'C'

         # D >= 60
         elif num >= 60:
                  return 'D'

         # F < 60
         else:
                  return 'F'

print('My grade: ', letter_grade(average(75, 77, 95, 100, 100, 88, 89, 83, 95)))

# Read DocString (like help())
print(average.__doc__)
print(letter_grade.__doc__)






         
