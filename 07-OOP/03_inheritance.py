class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)  # Call the parent class's __init__ method
        
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.model)
print(my_tesla.full_name())  # Output: Tesla Model S