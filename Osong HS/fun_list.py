# fun_list.py
"""
1. input() = 입력
2. while / for: = 반복
3. if / elif /  else = 조건
4. function = 함수
"""

def tiredQ():
    print("Are you tired?")
    tired = input("1 for yes, 0 for no: \n") # 문자열 받아
    tired = bool(tired) # boolean: T/F
    return tired

print("================================")
tired2 = tiredQ()
print(tired2, type(tired2))

while tired2:
    print("Don't sleep.")
    tired2 = bool(tiredQ())

print("Oh, I see.")
print("================================")
