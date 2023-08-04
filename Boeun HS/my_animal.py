# my_animal.py

class Animal:

    def __init__(self, name, kind='dog'):
        self.name = name
        self.kind = kind

    def get_name(self):
        print(f"My {self.kind}'s name is {self.name}.")

my_dog = Animal('Spot')
my_dog.get_name()
