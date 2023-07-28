# ECar = 전기차
from Car import Car

class ECar(Car):
    """ECar is a type of Car."""
    def __init__(self, make, model, year, battery_size=75):
        super().__init__(make, model, year)
        self.battery = battery_size

    def get_battery(self):
        print(f"Your battery is a {self.battery}-kWh battery.")
    
    def get_range(self):
        if self.battery <= 75:
            range = 260
        elif self.battery <= 100:
            range = 315
        elif self.battery <= 1_0000_0000:
            range = "unlimited "

        print(f"You can drive {range}km!")

ecar = ECar("tesla", "model x", 2024)
print(f"My e-car is a {ecar.get_name()}.")
ecar.get_battery()
ecar.get_range()
ecar.drive()