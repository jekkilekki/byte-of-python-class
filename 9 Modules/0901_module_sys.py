# 0901_module_sys.py

import sys

print('명령줄 인수는 다음과 같습니다: ')
for i in sys.argv:
         print(i)

print('\n\nPYTHONPATH는', sys.path, ' 입니다.\n')


if __name__ == '__main__':
         print('이 프로그램은 자체적으로 실행되고 있습니다.')
else:
         print('이 프로그램은 다른 모듈에서 가져오는 중입니다.')




from math import sqrt

num = int(input('숫자를 입력하세요: '))
print('{}의 제곱근은 {}입니다.'.format(num, sqrt(num)))
