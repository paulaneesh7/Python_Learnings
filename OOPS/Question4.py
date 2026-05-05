# Encapsulation

class Car:
    def __init__(self, model, brand):
        self.__model = model
        self.__brand = brand

    def display(self):
        print(f"Model: {self.__model}")
        print(f"Brand: {self.__brand}")

    # Getter method for brand
    def get_brand(self):
        return self.__brand

class ElectricCar(Car):
    def __init__(self, model, brand, battery):
        super().__init__(model, brand)
        self.__battery = battery  # Encapsulate the battery attribute

    def display(self):
        super().display()
        print(f"Battery: {self.__battery}")

    # Getter for battery
    def get_battery(self):
        return self.__battery


# Create an instance of ElectricCar
myTesla = ElectricCar("Model S", "Tesla", "100kWh")
myTesla.display()  # Display all details
print("Brand:", myTesla.get_brand())  # Access brand using getter
print("Battery:", myTesla.get_battery())  # Access battery using getter
