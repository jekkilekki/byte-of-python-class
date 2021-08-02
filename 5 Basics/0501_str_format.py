# 0501_format.py

'''This is a long comment.
We will learn `format` string.
Ready?
'''

age = 41
name = "Aaron"

print('{1} is {0} years old.'.format(age, name))

print(name + ' is ' + str(age) + ' years old.')

print('{name} is {age} years old.'.format(age = 28, name = 'IU'))

name2 = 'IU'
song = '가을아침'
print(f'{name2}\'s best song is {song}!!!')

print(name2 + "'s best song is " + song + '!'*30)
print('{0:_^20}'.format(song))

print('{0:_^20} is {1:*^10}\s best song~! {2:@^7} loves her!'
      .format(song, name2, name))














