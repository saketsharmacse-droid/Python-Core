numbers = list(map(int, input("Enter the input list: ").split()))
count = 0

for num in numbers:
    if num > 0:
        print(num)
        count += 1
print("Count of positive numbers:", count)