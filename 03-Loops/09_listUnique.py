items = input("Enter the input list elements: ")
input_list = items.split()

unique_item = set()
for item in input_list:
    if item in unique_item:
        print("Duplicate item found:", item)
    else:   
        unique_item.add(item)
