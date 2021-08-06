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
         def attr(self):
                  print('{}\n\
-------------------------------------------------\n\
|HP: {}\t|MP:  {}\t|EXP:  {}\t|\n\
|ATK: {}\t|MGC: {}\t|Heal: {}\t|\n\
-------------------------------------------------\n'\
                         .format(self.kind, self.hp, self.mp, self.exp, self.atk, self.mgc, self.heal))
         def is_dead(self):
                  return self.hp <= 0

tank = Warrior('Tank', 200, 20, 0, 60, 10, 10)
mage = Warrior('Mage', 120, 80, 0, 40, 40, 30)
fighter = Warrior('Fighter', 160, 50, 0, 50, 30, 20)

# Run program!!!
print('\nMYGAME에서 환영해요!')
name = input('히어로 이름 입력하세요: ')

while True:
         print('1. Tank')
         tank.attr()
         print('2. Mage')
         mage.attr()
         print('3. Fighter')
         fighter.attr()

         player_class = input('\n클래스를 선택하세요: 1, 2, 3.')

         if player_class == '1':
                  player_class = tank
                  print('환영합니다 {}, {}'.format(player_class.kind, name))
                  break
         elif player_class == '2':
                  player_class = mage
                  print('환영합니다 {}, {}'.format(player_class.kind, name))
                  break
         elif player_class == '3':
                  player_class = fighter
                  print('환영합니다 {}, {}'.format(player_class.kind, name))
                  break
         else:
                  print('유효한 클래스를 선택하세요.') 

# AI 선택
ai_classes = [tank, mage, fighter]
ai = ai_classes[r.randint(0,2)]

if ai == tank:
         print('당신은 Tank와 싸울 것입니다.')
elif ai == mage:
         print('당신은 Mage와 싸울 것입니다.')
elif ai == fighter:
         print('당신은 Fighter와 싸울 것입니다.')

# Game Loop
while True:
         # 사용자 차례
         action = input('뭐를 하고싶어요? 1. 공격 2. 마법 3. 회복')

         if action == '1':
                  # Attack
                  ai.hp = ai.hp - player_class.atk
         elif action == '2':
                  # Magic
                  ai.hp = ai.hp - player_class.mgc
         elif action == '3':
                  # Heal
                  player_class.hp = player_class.hp + player_class.heal
         else:
                  print('유효한 행동을 선택하세요.')
                  
         # AI 차례
         ai_action = str(r.randint(1,3))
         print('AI chose', ai_action)

         if ai_action == '1':
                  # Attack
                  player_class.hp = player_class.hp - ai.atk
         elif ai_action == '2':
                  # Magic
                  player_class.hp = player_class.hp - ai.mgc
         elif ai_action == '3':
                  # Heal
                  ai.hp = ai.hp + ai.heal
         else:
                  print('AI 잘못 선택 했다.')

         # Show HP
         print('\n당신의 HP는 {}입니다.'.format(player_class.hp))
         print('AI의 HP는 {}입니다.'.format(ai.hp))

         # R U Dead?
         if player_class.is_dead():
                  print('당신은 졌다.')
                  break
         elif ai.is_dead():
                  print('당신은 이겼다!!!!!')
                  break


























