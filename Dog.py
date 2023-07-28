# Dog Class
class Dog:
    """This is a Dog."""

    # Properties 속성
    def __init__(self, name='', age='', kind='', size='', gender='', looks=''):
        self.name = name
        self.age = age
        self.kind = kind
        self.size = size
        self.gender = gender
        self.looks = looks

    # Methods 함수 / 행동 
    def bark(self):
        print("멍멍! 멍멍!")

    def smell(self, obj=''):
        print(f"{self.name}가 {obj} 냄새를 맡고 있어요.")

    def lick(self, obj=''):
        print(f"{self.name}가 {obj}을 핥고 있어요.")

my_dog = Dog("Spot", 5, "Terrier", "small", "F", "cute")
print(my_dog.name)
my_dog.bark()
my_dog.smell()
my_dog.smell("apple")
my_dog.smell("another dog's butt")
my_dog.lick()

friend_dog = Dog("Fred")
print(friend_dog.name)
