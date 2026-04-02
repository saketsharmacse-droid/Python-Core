#solution1
# number = int(input("Enter the number:"))
#mult = list()

#for i in range (1, 11):
 #   if i != 5:
  #      mult.append(number*i)
        
#print("multiplication table of number " +str(number)+ " is " +str(mult))
        
#solution2
number = int(input("Enter the number:"))
mult = list()

for i in range (1, 11):
    if i != 5:
        print(number, "x", i, "=", number * i)
        
#solution3
number = int(input("Enter the number:"))

for i in range (1, 11):
    if i == 5:
        continue
    print(number, "x", i, "=", number * i)
        