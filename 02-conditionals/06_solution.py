distance = int(input("Enter the distance to your destination in kms: "))

if distance < 3:
    mode = "walk"
elif distance <= 15:
    mode = "bike"
else:
    mode = "car"
    
print("AI recommends you to travel via ",mode)