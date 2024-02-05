# py_game.py

# 게임 요구 사항
'''
    1. 캐릭터 클래스 - 속성 및 함수
    2. 텍스트 입력 - 선택
    3. 일련의 int 값 선택
    4. 무작위 결과
'''

import random as r

class Char:

    def __init__(self, kind, hp, mp, atk, heal):
        self.kind = kind
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.heal = heal

    def attr(self):
        hp_p = '| HP: ' + str(self.hp) + '\t'
        mp_p = '| MP: ' + str(self.mp) + '\t|'
        atk_p = '| ATK: ' + str(self.atk) + '\t'
        heal_p = '| HEAL: ' + str(self.heal) + '\t|'

        print(f'{self.kind}')
        print('---------------------------------')
        print(f'{hp_p}{mp_p}\n{atk_p}{heal_p}')
        print('---------------------------------')
        print()

    def is_dead(self):
        return self.hp <= 0

# Run program!!
print("\nPY GAME에서 환영합니다!~")

angel = Char('1. Angel', 200, 10, 20, 40)
angel.attr()

witch = Char('2. Witch', 100, 40, 30, 10)
witch.attr()

player_kind = input("\n사용자 종류를 선텍하십시오: ")

# Welcome!
if player_kind == '1':
    player = angel
    print("Angel 환영합니다!~")
    
elif player_kind == '2':
    player = witch
    print("Witch 환영합니다!~")
    
else:
    print("유효한 클래스를 선택하십시오.")
    
# AI 선택
ai_kind = [angel, witch]
ai = ai_kind[r.randint(0,2)]

if ai == angel:
    print("당신은 Angel와 싸울 것입니다!")
elif ai == witch:
    print("당신은 Witch와 싸울 것입니다!")

# Game Loop
while True:
    
    # 사용자 차례
    action = input("\n뭐를 하고싶십니까? 1. 공격 2. 마법 3. 회복 : ")

    if action == '1': # 공격
        ai.hp = ai.hp - player.atk
    elif action == '2': # 마법
        ai.hp = ai.hp - player.mp
    elif action == '3': # 회복
        player.hp = player.hp + player.heal      
    else: 
        print("유효한 행동을 선택하십시오.")

    # AI 차례
    ai_action = r.randint(1,3)

    if ai_action == 1: # 공격
        player.hp = player.hp - ai.atk
    elif ai_action == 2: # 마법
        player.hp = player.hp - ai.mp
    elif ai_action == 3: # 회복
        ai.hp = ai.hp + ai.heal      
    else: 
        print("AI가 선택을 잘못 했습니다.")

    # Show HP
    print(f'\n당신의 HP는 {player.hp}입니다.')
    print(f'AI의 HP는 {ai.hp}입니다.')

    # R U Dead?
    if player.is_dead():
        print('당신은 졌다.')
        break
    elif ai.is_dead():
        print('당신은 이겼다!!!!')
        break

