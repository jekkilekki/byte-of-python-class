# 1302_files.py

lyrics = '''\
"뭐해" 라는 두 글자에
"네가 보고 싶어" 나의 속마음을 담아 우
이모티콘 하나하나 속에
달라지는 내 미묘한 심리를 알까 우
'''

# 쓰기 Write
f = open('lyrics.txt', 'w')
f.write(lyrics)
f.close() 

# 읽기 Read
f = open('lyrics.txt') # Read is first
while True:
         line = f.readline()
         if len(line) == 0: # 0 is EOF (end of file)
                  break
         print(line, end = '')
f.close()





import io

emoji = '''\
😀 😃 😄 😁 😆 😅 😂 🤣 🥲 ☺️ 😊 😇 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🥸 🤩 🥳 😏 😒 😞 😔 😟 😕 🙁 ☹️ 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡 🤬 🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 😯 😦 😧 😮 😲 🥱 😴 🤤 😪 😵 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿 👹 👺 🤡 💩 👻 💀 ☠️ 👽 👾 🤖 🎃 😺 😸 😹 😻 😼 😽 🙀 😿 😾
'''

# 쓰기 Write
f = io.open('emoji.txt', 'wt', encoding = 'utf-8')
f.write(emoji)
f.close() 

# 읽기 Read
with io.open('emoji.txt', encoding = 'utf-8') as f: # Read is first
         for line in f:
                  print(line, end = '')




         
