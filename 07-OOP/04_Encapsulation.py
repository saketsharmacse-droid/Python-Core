class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand + " is the brand of the car."
    
my_Tesla = Car("Tesla", "Model S")
print(my_Tesla.get_brand())  # Output: Tesla is the brand of the car.
print(my_Tesla.brand)  # Output: Model S