# 1002_tuple.py

zoo = 'python', 'elephant', 'penguin'
print('Zoo has', len(zoo), 'animals.')
print('This is my zoo: ', zoo)

new_zoo = '뱀', '코끼리', '펭귄'
print('새로운 동물원은', len(new_zoo), '동물이 있습니다.')
print('이것은 내 동물원 입니다: ', new_zoo)

big_zoo = zoo, new_zoo
print('Big zoo has', (len(big_zoo[0]) + len(big_zoo[1])), 'animals.')
print('This is my zoo:', big_zoo)

print('내가 가장 좋아하는 동물은', big_zoo[0][0])
