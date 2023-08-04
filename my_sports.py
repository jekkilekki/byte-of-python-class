# my_sports.py

soccer, mlb, nba = ["Jeonbuk", "Seoul", "Jeju"], [], []

print(soccer)

# 변경할 수 있는 것
soccer[0] = "Liverpool"
soccer[1] = "Real Madrid"
soccer[2] = "Bayern Munchen"

print(soccer)

# 추가할 수 있는 것
mlb.append("Angels")
mlb.append("Dodgers")
mlb.append("Rangers")
print(mlb)

# 위치 선택 추가
mlb.insert(1, 'Red Sox')
print("Sorted:", sorted(mlb, reverse=True)) # 순서대로 
print("Original:", mlb)

nba = [
    "Warriors",
    "Nuggests",
    "Bulls",
    "Celtics"
]
print("Sorted:", nba.sort())
print("Original:", nba)

nba.append("Heat")
print(nba)

# 삭제하기
# del nba['Warriors']

# C++:
# for(int i = 0; i < 10; i++) { ... }

for i in range(0,2):
    del nba[0]
    del nba[-1]

print(nba)

nfl = [
    "Broncos",
    "Saints",
    "Giants",
    "Eagles",
    "Chiefs"
]
print(nfl)

nfl.remove('Saints') # not index, use name
print(nfl)

print("The Superbowl winner was: ", nfl.pop())
print(nfl)

print("The biggest team: ", nfl.pop(1))
nfl.reverse()
print(nfl)

print(f"Only {len(nfl)} teams left.")