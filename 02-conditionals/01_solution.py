age = int(input("Provide me the age : "))

if (age < 13):
    print("Child")
elif age < 20: #yaha pe 20 not included hai, kyuki 20 se 1 zyada age ke log teenager nahi hote hai
    print("Teenager")
elif age<59:
    print("adult")
else:
    print("Senior Citizen")