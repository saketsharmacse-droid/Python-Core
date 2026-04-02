weather = input("What is the weather like today? ").lower()

if weather == "sunny":
    activity = "go for a walk"
elif weather == "rainy":    
    activity = "stay indoors and read a book"  
elif weather == "snowy":
    activity = "build a snowman"
    
print(activity)