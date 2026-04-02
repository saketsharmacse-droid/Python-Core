class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
my_car = Car("Toyota", "Corolla")
print(my_car.full_name())  # Output: Toyota Corolla

my_newCar = Car("Honda", "Civic")
print(my_newCar.full_name())  # Output: Honda Civic