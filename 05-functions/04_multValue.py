import math

def function1(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    
    return area, circumference
    print("hi") # This line will never be executed because it's after the return statement
    
a,c = function1(3)
print("Area: ", a, "\ncircumference: ", c)
