def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

#factory functions / closure functions

f = chaicoder(2) #num = 2
g = chaicoder(3) #num = 3

print(f(3))
print(g(3))