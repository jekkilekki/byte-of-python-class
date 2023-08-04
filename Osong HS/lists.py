# Desktop/aaron/lists.py
'''
3과 = 목록

We will study Lists.
리스트는 대괄호로 생성한다.
'''
sports = ['soccer', 'bball', 'dodgeball', 'health']
print(sports[0:3]) # index:몇개
print() # \n
print()
print()
print(sports[-4])
# 변경하기
sports[1] = 'baseball' # index에서 변경
print(sports)

sports.append('hiking') # 마지막에서 추가 
print(sports)

sports.insert(1, 'tennis') # index에서 추가
print(sports)

# 삭제하기
del sports[0] # index 삭제
last_sport = sports.pop(2) # 마지막 삭제 / index 삭제
print(last_sport)
print(sports)

sports.remove('tennis') # item 삭제 
print(sports)