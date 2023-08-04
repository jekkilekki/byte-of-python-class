first = "Aaron" # capitalize / title()
last = "Snowberger"
food = "fried chicken" # lower()
movie = "JOHN WICK" # upper()

print(food.upper())
print(movie.lower())
print("I like", movie.title())

print("I like" + "\n\t" + food + "\n\t" + movie)

# Format string 서식하는 문자열

# 객체.format(매개 변수) 함수 Python version < 3.5
# print()
print("Hello, {}".format(first))
print("Hello, {} {}. Do you like {} and {}?"
    .format(first, last, food, movie))

# f-string = Python version > 3.6
print(f"Hello, {first.upper()} {last}. Do you like {food} and {movie.title()}?")

music1 = 'hip-hop              '
music2 = '                 rock'
music3 = '       classic       '

print(music1.rstrip(), music2.lstrip(), music3.strip())

music4 = 'k-pop           indie'
print(music4.replace(" ", "-"))
