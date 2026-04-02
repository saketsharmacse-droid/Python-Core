age = int(input("Enter your age: "))
day = input("Enter the day of the week: ").lower()

price = 12 if age >= 18 else 8 ####this is a revision point

if day == "wednesday":
    price -= 2
else:
    price += 0

    
print(" Ticket price for you is: $",price)
