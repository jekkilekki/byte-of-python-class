# my_stars.py

def best_stars():
    while True:
        star = "Who's your favorite star?\n"
        star += "Press 'q' to QUIT. "
        my_star = input(star)

        if my_star.lower() == 'q':
            break

        if my_star.lower() == '박근혜':
            print("What???! No!!")
            break

        if my_star.lower() == 'you':
            print("I love you too!")

        print(f"Wow! I like {my_star} too!")

best_stars()