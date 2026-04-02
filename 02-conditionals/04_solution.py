fruit = input("Enter the name of the fruit: ").lower()
color = input("Enter the color of the fruit: ").lower()

if fruit == "banana":
    if color == "green":
        print("unripe")
    elif color == "yellow":
        print("ripe")
    elif color == "brown":
        print("overripe")   
        
else:
    print("Sorry, I don't have information about that fruit.")