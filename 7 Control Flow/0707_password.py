# 0707_password.py

for i in range(0,5): # 5 chance
         pw = input('Choose password: ')

         if pw == 'quit':
                  break

         if len(pw) < 8:
                  print('Password too small')
                  continue

         print('Welcome to Instagram!')

else:
         print('Too many wrong passwords. Website locked.')
