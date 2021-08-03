# 0701_if.py

number = 110
guess = int(input("What's your guess? "))

if guess == number:
         print('Yes! Correct!')

elif guess < number:
         print('No, guess is too small.')

else:
         print('No, guess is too big.')

print('Done')
