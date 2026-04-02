#decorators padhna hai
#self, constructors, init sab padhna hai, static method bhi
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
    
    @staticmethod
    def description():
        return "Cars are a means of transportstion"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        self.battery_size = battery_size
        super().__init__(brand, model)  # Call the parent class's __init__ method
        
    
    def fuel_type(self):
        return "Electric Charge"  
    
print(Car.description)  # Accessing the description method directly from the class
access = Car.description() # Calling the description method without creating an instance