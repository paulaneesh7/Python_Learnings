

class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def display(self):
        print(f"Model: {self.model}")
        print(f"Brand: {self.brand}")


# Object
myCar = Car("A8", "Audi")
myCar.display()