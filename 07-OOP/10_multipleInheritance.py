class Car:
    
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"   
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)  # Call the parent class's __init__ method
        
    
    
        
class Battery:
    def battery_info(self):
        return "This is a battery class"

class Engine:
    def engine_info(self):
        return "This is an engine class"

class ElectricCar2(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar2("Tesla", "Model S")

print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
    
