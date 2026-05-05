
# Always keep the name of class in captial letter (first Alphabet)
class Car:

    # Constructor (self is like "this" in Java)
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model



# Creating object of class Car
myCar = Car("Toyota", "Corolla")
print(myCar.brand)
print(myCar.model)


myNewCar = Car("Honda", "Civic")
print(myNewCar.brand)
print(myNewCar.model)
