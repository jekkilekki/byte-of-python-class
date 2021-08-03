# 0704_break.py

name = 'Aaron'

while True:
         string = input('Your name: ')

         if string == name:
                  print('Welcome {}!'.format(name))
                  break

         elif string == 'quit':
                  print('Leave you hacker!')
                  break

         print('String length is ', len(string))

print('Done')
