# 1003_dict.py

students = {
         '10804': '김현성',
         '10810': '오성현',
         '10812': '이서준',
         '10911': '손태성',
         '10915': '임다운',
}

def get_names():
         for name in students.values():
                  print(name)

def get_nums():
         for num in students.keys():
                  print(num)

def get_list():
         for num, name in students.items():
                  print("{}'s number is {}.".format(name, num))

def get_num_list():
         for i, (num, name) in enumerate(students.items()):
                  print("{}: {}'s number is {}.".format(i, name, num))


students['19811224'] = 'Aaron'

get_num_list()

def del_student(num):
         if num in students:
                  del students[num]

del_student('10915')
get_num_list()


students['10804'] = {
         'name': '김현성',
         '발열체크': (36.7, 36.8, 36.6, 36.7)
}

print(students)











