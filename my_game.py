# my_game.py

"""
How to run:
1. Char class - 속성 Attributes + 함수 Functions
2. Text input - User selection
3. Random results - Fight, Defend, Heal...
"""

import random as r

class Player:
    """
    Simple Player / Warrior / Fighter class.
    """
    def __init__(self, kind, hp, mp, exp, atk, mgc, heal):
        self.kind = kind
        self.hp = hp
        self.mp = mp
        self.exp = exp
        self.atk = atk
        self.mgc = mgc
        self.heal = heal

    def stats(self):
        string = f"{self.kind}\n"
        string += f"-------------------------\n"
        string += f"| HP: {self.hp}\t| MP: {self.mp}\t| EXP: {self.exp} |\n"
        string += f"| ATK: {self.atk}\t| MGC: {self.mgc}\t| Heal: {self.heal} |\n"
        string += f"-------------------------\n"
        print(string)

    def is_dead(self): # R U Dead?
        return self.hp <= 0 # T/F
    
# Make Char
# kind, hp, mp, exp, atk, mgc, heal
iron = Player('Iron Man', 150, 20, 0, 40, 0, 10)
capt = Player('Captain America', 130, 15, 0, 30, 10, 15)
groot = Player('IMGroot', 200, 25, 0, 50, 10, 30)
hulk = Player('Hulk', 180, 0, 0, 45, 0, 5)

# Run program!!
msg = '\nWelcome to Marvel Fighter!'
msg += '\nAre you ready?'
msg += '\nWho will you choose?\n'
print(msg)

chars = [iron, capt, groot, hulk]

for i, c in enumerate(chars):
    print(f'{i+1}.')
    c.stats()

# Choose char
while True:
    player = input('\nChoose your fighter. 1, 2, 3, 4')
    player = int(player)

    if player == 1:
        player = iron
    elif player == 2:
        player = capt
    elif player == 3:
        player = groot
    elif player == 4:
        player = hulk
    
    if not isinstance(player, int):
        print(f"Welcome {player.kind}")
        break
    else:
        print("Enter a correct number!")

# AI Choice
ai = chars[r.randint(0, len(chars))] # (0, 4) = 0, 1, 2, 3
print(f"You will fight {ai.kind}!")
print("Ready? FIGHT!!")

# Game Loop
while True:
    # Player choice
    action = input("1. Attack, 2. Magic, 3. Heal")
    action = int(action)

    if action == 1:
        ai.hp -= r.randint(player.atk/2, player.atk*2)
    elif action == 2:
        ai.hp -= r.randint(player.mgc/2, player.mgc*2)
    elif action == 3:
        player.hp += r.randint(player.heal/2, player.heal*2)
    else:
        print("You chose a wrong number. Skip your turn!")

    # AI Turn
    ai_action = r.randint(1,4) # 1, 2, 3 

    if ai_action == 1:
        player.hp -= r.randint(ai.atk/2, ai.atk*2)
    elif ai_action == 2:
        player.hp -= r.randint(ai.mgc/2, ai.mgc*2)
    elif ai_action == 3:
        ai.hp += r.randint(ai.heal/2, ai.heal*2)
    else:
        print("AI chose a wrong number. Skip AI turn!")

    # See HP/damage
    print(f'You: {player.hp}HP')
    print(f'AI: {ai.hp}HP')

    # R U Dead?
    if player.is_dead():
        print("You're dead. You lose. You loser. OTL.")
        break
    elif ai.is_dead():
        print("AI is dead! You win! Winner!!!!!!")
        break