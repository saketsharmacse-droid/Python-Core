str_input = input("Enter your String: ")



for char in str_input:
    #print(char)
    if str_input.count(char) == 1:
        print("First non-repeated character is: ", char)
        break #breaks the loop so that it does not check for the remaining characters after finding the first non-repeated character
        