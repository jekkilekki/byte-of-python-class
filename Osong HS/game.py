# game.py

# 게임 요구 사항
"""
1. 캐릭터 클래스 - 속성 및 행동 (함수)
2. 텍스트 입력 - 사용자 선택, 캐릭터 이름 등
3. 일련의 int 값(1, 2, 3, ...)으로 선택
4. 무작위 결과 - 공격, 주문, 방어, 치유는 무작위 양의 손상 또는 복원을 수행한다.
"""

import random as r

class WarFighter:
    """Simple Warrior AND Fighter class."""
    def __init__(self, kind, hp, mp, exp, atk, mgc, heal):
        self.kind = kind
        self.hp = hp 
        self.mp = mp 
        self.exp = exp
        self.atk = atk 
        self.mgc = mgc 
        self.heal = heal

    def attr(self):
        string = f"{self.kind}\n"
        string += f"--------------------------------\n"
        string += f"|HP: {self.hp}\t|MP: {self.mp}\t|EXP: {self.exp}\t|\n"
        string += f"|ATK: {self.atk}\t|MGC: {self.mgc}\t|Heal: {self.heal}\t|\n"
        string += f"--------------------------------"

        print(string)

    def is_dead(self): # R U Dead?
        return self.hp <= 0 # T/F

# Make Characters 캐릭터 만들기
# kind, hp, mp, exp, atk, mgc, heal
wolverine = WarFighter('Wolverine', 150, 0, 0, 25, 5, 15)
deadpool = WarFighter('Deadpool', 140, 10, 0, 25, 10, 10)
quicksilver = WarFighter('Quick Silver', 100, 20, 0, 10, 10, 10)
spiderman = WarFighter('Spiderman', 110, 5, 0, 10, 10, 10)
hulk = WarFighter('Hulk', 300, 0, 0, 50, 10, 0)

# RUN program!!
msg = "\nWelcome to WarFighter!"
msg += "\nAre you ready?"
msg += "\nWho will you be?\n"
print(msg)

chars = [wolverine, deadpool, quicksilver, spiderman, hulk]

for i, char in enumerate(chars):
    print(f"{i+1}.")
    char.attr() # print() 함수 있어서 함수 콜만 할 수 있어요

# 캐릭터 선택
while True:
    player = input('\n플레이어를 선택하세요: 1, 2, 3, 4, 5.')
    player = int(player)

    if player == 1:
        player = wolverine
        print(f"Welcome {player.kind}!")
        break
    elif player == 2:
        player = deadpool
        print(f"Welcome {player.kind}!")
        break
    elif player == 3:
        player = quicksilver
        print(f"Welcome {player.kind}!")
        break
    elif player == 4:
        player = spiderman
        print(f"Welcome {player.kind}!")
        break
    elif player == 5:
        player = hulk
        print(f"Welcome {player.kind}!")
        break
    else: 
        print("유효한 플레이어를 선택하세요.")

# AI Player
# len(chars) = 5 
# chars[5] # 오류 chars[4]까지만 할 수 있어서 len(chars)-1
ai = chars[r.randint(0, len(chars)-1)]
print(f"You will fight {ai.kind}.")

# Game Loop:
while True:
    # 사용자 차례
    action = input("뭐를 하겠어요? 1. 공격, 2. 마법, 3. 회복")
    action = int(action)

    if action == 1: # Attack
        ai.hp -= r.randint(player.atk/2,player.atk*2) # -10 r.randint(player.atk/2,player.atk*2)
    elif action == 2: # Magic
        ai.hp -= player.mgc
    elif action == 3: # Heal
        player.hp += player.heal
    else:
        print("유효한 행동을 선택하세요.")

    # AI 차례
    ai_action = r.randint(1,4) # 1, 2, 3

    if ai_action == 1: # Attack
        player.hp -= ai.atk
    elif ai_action == 2: # Magic
        player.hp -= ai.mgc
    elif ai_action == 3: # Heal
        ai.hp += ai.heal
    else:
        print("AI가 잘못 선택했나봐요.....ㅠㅠ OTL")

    # Show HP
    print(f"You: {player.hp}HP")
    print(f"AI: {ai.hp}HP")

    # R U Dead?
    if player.is_dead():
        print("You're dead. 졌다. ㅠㅠ OTL......")
        break
    elif ai.is_dead():
        print("You win! CHAMPION!")
        break