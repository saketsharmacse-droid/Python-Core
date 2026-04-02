pet_type = input("Enter the type of pet you have (dog/cat): ").lower()
pet_age = int(input("Enter the age of your pet: "))

if pet_type == "dog":
    if pet_age < 2:
        food = "puppy food"
    elif pet_age < 7:
        food = "adult dog food"
    else:
        food = "senior dog food"
elif pet_type == "cat":
    if pet_age < 1:
        food = "kitten food"
    elif pet_age < 10:
        food = "adult cat food"
    else:
        food = "senior cat food"
        
print("you should feed your " + pet_type+ " " +food+ ".")