#keyWord Args
def fun1(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
fun1(name='Saket', age = 24, power = "laser")
fun1(name = "shaktiman")
fun1(name = "Saket", age = 24, power = "laser", city = "Delhi")