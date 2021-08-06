# 1304_unicode.py

import io # input/output

emoji = '''\
🤬 🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 😯 😦 😧 😮 😲 🥱 😴 🤤 😪 😵 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿 👹 👺 🤡 💩 👻 💀 ☠️ 👽 👾 🤖 🎃 😺 😸 😹 😻 😼 😽 🙀 😿 😾
'''

# 쓰기 Write
f = io.open('emoji.txt', 'wt', encoding = 'utf-8')
f.write(emoji)
f.close() 

# 읽기 Read
with io.open('emoji.txt', encoding = 'utf-8') as f:
         for line in f:
                  print(line, end = '')
                  
'''
f = io.open('emoji.txt', 'rt', encoding = 'utf-8') # Read is first
while True:
         line = f.readline()
         if len(line) == 0: # 0 is EOF (end of file)
                  break
         print(line, end = '')
f.close()
'''




         
