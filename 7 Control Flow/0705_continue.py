# 0705_contine.py

password = 'H@ck34!' # '4@r0n'

while True:
         pw = input('Password: ')

         if pw == 'quit':
                  print('Login canceled.')
                  break

         if len(pw) < len(password):
                  print('Password too small.')
                  continue

         print('Welcome to Instagram!')
