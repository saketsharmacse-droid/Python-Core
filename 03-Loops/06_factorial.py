number = int(input("Enter the number: "))
factorial = 1
i = number

while i > 0:
    factorial *= i
    i -= 1
print("Factorial value of ", number,  "is:", factorial)
