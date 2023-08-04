# 연예인 = stars = celebrities

def make_star(name, job, age='', weight=''):
    # 사전 (객체와 비슷) 키:값
    person = {
        'name': name,
        'job': job
    }

    if age != '':
        person['age'] = age

    if weight != '':
        person['weight'] = weight
    
    return person # 반환 값

jinsu = make_star('김진수', '축구선수', 30, 72)
print(jinsu)

troye = make_star('Troye Sivan', 'singer', 28)
print(troye)

hugh = make_star('Hugh Jackman', 'Wolverine')
print(hugh)