after = input("수업 끝나고 뭐를 할까요?\n'q'는 'quit'\n")
'먹고'
do = []

while True:
    if after == 'q':
        break
    else:
        do.append(after)
        after = input("또?")

# print(do) # ['eat', 'sleep', 'game']

print(f'와!~ 너무 많이 하네요! 당신은 {len(do)}개나 하죠?')
print('당신은 ')

for haengdong in do:
    if haengdong == '먹고' or haengdong == '먹다':
        food = input('뭐를 먹을거예요?')
        print(f'{food}를 맛있게 드세요~~~')
    elif haengdong == '자고' or haengdong == '자다':
        print('잘자!')
    elif haengdong == '게임하고' or haengdong == '게임하기' or haengdong == '게임하다':
        print('게임하면 안 되는데요!~')
    else:
        print('재밌게 하세요~')