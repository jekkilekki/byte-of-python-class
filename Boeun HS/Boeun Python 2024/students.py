# dictionary (사전 = 속성 있는 객체)

students = {
    0: {
        'name': '서완호',
        'age': 18,
        'height': 177,
        'hobbies': [
            'games',
            'sleep'
            ]
        },
    1: {
        'name': '설진길',
        'age': 18,
        'height': 163,
        'hobbies': [
            'games',
            'sleep'
            ]
        },
    2: {
        'name': '이승희',
        'age': 18,
        'height': 172,
        'hobbies': [
            'games',
            'sleep'
            ]
        },
    3: {
        'name': '박천관',
        'age': 18,
        'height': 173,
        'hobbies': [
            'games',
            'making movies',
            'sleep'
            ]
        },
    4: {
        'name': '김민철',
        'age': 18,
        'height': 170,
        'hobbies': [
            'games',
            'fishing',
            'sleep'
            ]
        },
    5: {
        'name': '권세나',
        'age': 18,
        'height': 165,
        'hobbies': [
            'games',
            'makeup',
            'sleep'
            ]
        },
    6: {
        'name': '에런',
        'age': 34,
        'height': 180,
        'hobbies': [
            'coding',
            'exercise',
            'reading'
            ]
        }
    }

print(f"My class has {len(students)} students.")

print(f"{students[4]['name']} likes {students[4]['hobbies'][1]}.")

for std, std_info in students.items():
    print(f"{std_info['name']} is {std_info['height']}cm.")

    if 'sleep' not in std_info['hobbies']:
        print(f"Is {std_info['name']} an adult?")




      
