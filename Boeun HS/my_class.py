# my_class.py

# 조건문 (if-elif-else)
# 사전 (dictionary)

students = {
    'gw': {
        'name': 'Gun Woong',
        'last_name': 'Sung',
        'age': 17,
        'job': "Mom's Touch",
        'hobbies': ['playing guitar', 'sleeping', 'reading']
    },
    'as': {
        'name': 'Aaron',
        'last_name': 'Snowberger',
        'age': 43,
        'job': None,
        'hobbies': ['특강']
    }
}

print("My class has", len(students), "students.")
print("The first student is", students['gw']['name'])

for std, std_info in students.items():
    print("Student name:", std_info['name'])
    print("Student job:", std_info['job'])

    # 조건문 (age)
    if std_info['age'] < 18:
        print(f"{std_info['name']} is too young to work. Go home.")
    elif std_info['age'] < 65:
        print(f"{std_info['name']} is too young to retire. Find a job!")
    else:
        print(f"{std_info['name']} is old. Enjoy retirement!")