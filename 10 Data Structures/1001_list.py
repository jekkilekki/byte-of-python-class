# 1001_list.py

# 이것은 내 쇼핑 목록입니다.
shoplist = ['chicken breast', '닭가슴살', '참치', 'eggs', 'rice', '빵']

shoplist.sort()

print('I need ', len(shoplist), ' things.') # 몇개

def print_list():
         print('This is my list: ', end = '')
         for item in shoplist:
                  print(item, end = ' ')

def append_sort(item):
         shoplist.append(item)
         shoplist.sort()

print('I also need peach.')
append_sort('peach')
print_list()

append_sort('아이스크림')
append_sort('apple')
append_sort('수박')
append_sort('파인애플')
append_sort('눈물이 계속 나오는 쇼킹 핫 양념 치킨')
print_list()

def pretty_print():
         print('\n')
         for i, item in enumerate(shoplist):
                  print(i+1, ':', item, end = '\n')

pretty_print()

# 매운 치킨을 안 좋아해서 
del shoplist[5]

pretty_print()

last_item = shoplist.pop(4)
pretty_print()
print('I just bought ', last_item)

shoplist.insert(4, '삼겹살')
pretty_print()




