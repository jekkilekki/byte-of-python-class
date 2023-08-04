# Car class
class Car:
    """
    docstring: 잛은 설명
    
    This is a basic car.
    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.km = 0
        self.tank = 100

    def get_name(self):
        # 'bMw'.lower() = 'bmw' == 'bmw' 
        if self.make.lower() == 'bmw':
            self.make = self.make.upper()
        else:
            self.make = self.make.title()

        return f"{self.year} {self.make} {self.model.title()}"

    def drive(self):
        self.km += 100 # self.km = self.km + 100
        self.tank -= 10

        print(f"You drove {self.km}km, and have {self.tank}% gas left.")

        if self.tank <= 0:
            print("You have NO gas! Stop!")

my_car = Car("ford", "mustang", 1969)
my_car2 = Car("bmw", "i5", 2024)

name = my_car.get_name()
name2 = my_car2.get_name()

print(f"My old car is a {name}.")
print(f"My new car is a {name2}.")

"""
C++에서 이렇게 for loop 만들 수 있다:

for(var i = 0; i < 12; i++) {
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
}

파이썬 에서:
for i in range(0, 12):
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
"""
for i in range(0, 12):
    my_car2.drive()