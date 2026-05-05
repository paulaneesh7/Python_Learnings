

# Polymorphism

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
    
    def fuel_type(self):
        return "Fuel type: Petrol or Diesel"
    

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

    
    def fuel_type(self):
        return "Fuel type: Electric"
    
myTesla = ElectricCar("Model S", "Tesla", "100 kWh")
myTesla.display()
print(myTesla.fuel_type())

safari = Car("Safari", "Tata")
safari.display()
print(safari.fuel_type())