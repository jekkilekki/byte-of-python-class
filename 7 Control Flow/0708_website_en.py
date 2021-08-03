# 0706_login.py

'''Program to create a user account and login the user.

Create user account (while loop).
1. Create username (input -> variable).
2. If password length > 8, create password (input -> variable).
3. Print account creation message.

Login (while loop).
1. If input == username, continue to password.
2. If input == password, login (for loop, 3 chances).
3. Print success message.
'''

username = ''
password = ''

while True:
         print('=============================')
         print('Welcome to Instagram!')
         print('=============================')
         choice = int(input('0 = cancel. 1 = create account. 2 = login\n'))

         if 0 == choice:
                  print('Canceled.')
                  break

         if 1 == choice:
                  # Create account
                  print('\nCreate your Instagram account.')
                  print('------------------------------')
                  username = input('Enter your username: ')
                  
                  while 4 > len(username):
                           username = input('Username too short.\n\
                                            Enter your username: ')
                           if 'quit' == username:
                                    break

                  print('Your username is {}.\n'.format(username))
                  password = input('Enter your password: ')

                  while 8 > len(password) and password != 'password':
                           password = input('Password too short.\n\
                                            Enter your password: ')
                           if 'password' == password:
                                    print('Please choose a stronger password!')
                           if 'quit' == password:
                                    break
                           
                  print('Your password is {}.\n'.format('*'*len(password)))
                  print('Congratulations, your account is created!\n\n\n')

         if 2 == choice:
                  # Login
                  print('\nLogin to Instagram.')
                  print('------------------------------')
                  un = input('Enter your username: ')

                  while un != username:
                           print('That username does not exist.')
                           un = input('Enter your username: ')

                  pw = input('Enter your password: ')
                  for i in range(0,5):
                           if pw != password:
                                    print('Wrong password!')
                                    pw = input('Enter your password: ')
                           else:
                                    break
                  else:
                           print('You entered the wrong password too many times.\n\n')
                           continue

                  print('Welcome to Instagram, {}!'.format(username))
                  break

         if choice == 3:
                  print('Current username {}.\nCurrent password {}.'.format(username, password))
