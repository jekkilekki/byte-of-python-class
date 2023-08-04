# my_players.py

def best_player(name, position, sport="soccer", team='', number=None):
    best = f"My favorite player is {name}.\n"
    best += f"{name} plays {sport}"

    if team != '':
        best += f" on {team}.\n"
    else:
        best += '.\n'

    best += f"{name}'s position is {position}"
    
    if number is not None: 
        best += f" and number is {number}.\n"
    else:
        best += '.\n'

    print(best)

best_player("이강인", "mid-fielder", "soccer", "PSG", 19)
best_player("조규성", "striker")
best_player(sport="baseball", name="오타니", team="the Angels", number=17, position="pitcher and DH")
