

# Inheritance

class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def display(self):
        print(f"Model: {self.model}")
        print(f"Brand: {self.brand}")


# This is how we inherit a class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


# Object
myTesla = ElectricCar("Tesla", "Model S", 100)
myTesla.display()
