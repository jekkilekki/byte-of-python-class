# 0702_while.py

password = 12345678
running = True

while running:
         guess = int(input('Enter password: '))

         if guess == password:
                  print('Welcome to Facebook!')
                  running = False

         else:
                  print('Wrong password.')

else:
         print('Not logging in.')

print('Done')
