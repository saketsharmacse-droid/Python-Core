number = int(input("Enter the number: "))
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
print(is_prime,", it is not a prime number") if not is_prime else print(is_prime,", it is a prime number")