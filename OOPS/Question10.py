# Multiple Inheritance in Python

class Battery:
    def __init__(self, battery):
        self.__battery = battery
    
    def get_battery(self):
        return self.__battery

    
class Engine:
    def __init__(self, engine):
        self.__engine = engine
    
    def get_engine(self):
        return self.__engine


class ElectricCar(Battery, Engine):
    def __init__(self, battery, engine):
        # Explicitly initialize both parent classes
        Battery.__init__(self, battery)
        Engine.__init__(self, engine)
    
    def get_details(self):
        print("Battery: ", self.get_battery())  # Use appropriate method from Battery
        print("Engine: ", self.get_engine())   # Use appropriate method from Engine


# Create an instance of ElectricCar
car = ElectricCar(100, "Electric")
car.get_details()
