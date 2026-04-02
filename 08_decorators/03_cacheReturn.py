import time

def cache(func):
    cach_value = {}
    print(cach_value)
    def wrapper(*args):
        if args in cach_value:
            return cach_value[args]
        result = func(*args)
        cach_value[args] = result
        return result
    return wrapper



@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b
    
print(long_running_function(1, 2))
print(long_running_function(1, 2))
print(long_running_function(2, 3))