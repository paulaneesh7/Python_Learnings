


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage




class Vehicle_child(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)


Bus = Vehicle_child("Volvo AC", 320, 20)
print(Bus.name, Bus.max_speed, Bus.mileage)