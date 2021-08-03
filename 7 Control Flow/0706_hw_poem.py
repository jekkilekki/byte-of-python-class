# 0706_hw_poem.py

string = ''
i = 1

while True:
         s = input('Enter poem/lyrics line:')
         if s == 'quit':
                  break
         string = string + '\n' + s
print(string)
         
