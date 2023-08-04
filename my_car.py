# my_car.py

class Car:
    """
    A simple car class.
    """

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        self.km = 0
        self.oil = 50
        self.tank = 50

    def get_name(self):
        print(f"My car is a {self.year} {self.make} {self.model}.")

    def drive(self, hours):
        """
        hours: in hours (시간)
        """
        self.km += 100 * hours
        self.oil -= (10 * hours)

        print(f"In {hours} hours, you:")
        print(f"- drove {self.km}km")
        print(f"- used {self.tank - self.oil}L of gas")

my_car = Car(2023, "Mercedes", "Maybach SUV")
my_car.get_name()
my_car.drive(10)