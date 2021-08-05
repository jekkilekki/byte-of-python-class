# 1007_more_strings.py

best_kpop = 'BTS'

if best_kpop.startswith('B'):
         print('I love', best_kpop)
else:
         print('Who is that?')

girl_group = 'STAYC'

if girl_group.startswith('STA'): # 시작하는 것 
         print('Is it STAYC?')

if girl_group.endswith('YC'): # 끝나는 것
         print('It is STAYC!')
else:
         print('No, it is my friend Stacy.')

if girl_group.find('AY') != -1: # 찾는 것
         print('AY'*len(girl_group))

kpop_list = ['BTS', 'STAYC', '2NE1', '다비치']
kpop_sm = []
for k in kpop_list:
         sm = k.lower() # 소문자 ('Stayc', 'stayc', 'STAYC')
         kpop_sm.append(sm)
         print(sm) 

print(kpop_sm)
for s in kpop_sm:
         print(s.upper()) # 대문자


char = '**__!!'
print(char.join(kpop_list))













