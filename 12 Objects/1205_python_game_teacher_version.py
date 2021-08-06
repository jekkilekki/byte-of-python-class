# python_game.py

# 게임 요구 사항
'''
1. 캐릭터 클래스 - 속성 및 동작
2. 텍스트 입력 - 사용자 선택, 캐릭터 이름 등
3. 일련의 int 값(1, 2, 3...)으로 선택
4. 무작위 결과 - 공격, 주문, 치유는 무작위 양의 손상 또는 복원을 수행합니다.
'''

import random as r

class Warrior:
         def __init__(self, kind, hp, mp, exp, atk, mgc, heal):
                  self.kind = kind
                  self.hp = hp
                  self.mp = mp
                  self.exp = exp
                  self.atk = atk
                  self.mgc = mgc
                  self.heal = heal
         def print_attr(self):
                  print('{}\n\
-------------------------------------------------\n\
|HP: {}\t|MP:  {}\t|EXP:  {}\t|\n\
|ATK: {}\t|MGC: {}\t|Heal: {}\t|\n\
-------------------------------------------------\n'\
                         .format(self.kind, self.hp, self.mp, self.exp, self.atk, self.mgc, self.heal))
         def is_dead(self):
                  return self.hp <= 0

tank = Warrior('Tank', 200, 20, 0, 60, 10, 10)
tank.attr()

mage = Warrior('Mage', 120, 80, 0, 40, 40, 30)
mage.attr()

fighter = Warrior('Fighter', 160, 50, 0, 50, 30, 20)
fighter.attr()








