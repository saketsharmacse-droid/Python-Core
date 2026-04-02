order_size = input("Enter the order size: (Small/Medium/Large) ").lower()
extra_shot = input("Do you want an extra shot? (yes/no): ")

if extra_shot.lower() == "yes":
    coffee = order_size + " Coffee with an Extra Shot"
else:
    coffee = order_size + " Coffee"
    
print("You Ordered a " +coffee+ ".")