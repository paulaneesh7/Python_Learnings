

class Vehicle :
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


toyota = Vehicle(300, 18)
print(toyota.max_speed, toyota.mileage)