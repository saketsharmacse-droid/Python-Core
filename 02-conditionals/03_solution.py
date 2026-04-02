score = int(input("Enter your marks: "))

if score >= 101:
    print("Invalid marks entered. Please enter a value between 0 and 100.")
    exit()

##if score< 60:
    #print("Grade is F for your marks",score)
#elif score<70:
   # print("Grade is D for your marks",score)
#elif score<80:
    #print("Grade is C for your marks",score)
#elif score<90:
    #print("Grade is B for your marks",score) 
#else:
    #print("Grade is A for your marks", score)
    
    
if score >= 90:
    grade = 'A'
elif score >= 80:  
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
    
print("Grade is",grade,"for your marks",score)