#attributes are variables that belong to an object
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    #init is a constructor method that is called when an object is created. It is used to initialize the attributes of the class. The __init__ method takes in parameters that are used to set the values of the attributes. In this case, the brand and model of the car are passed as parameters and assigned to the self.brand and self.model attributes of the class.
        
    #self is like the "this" keyword in other programming languages, it refers to the current instance of the class. It is used to access the attributes and methods of the class.
my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

my_newCar = Car('Tata', 'Safari')
print(my_newCar.model)
print(my_newCar.brand)