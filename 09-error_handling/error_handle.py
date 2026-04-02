file = open('uoutube.txt', 'w')

try:
    file.write(" Saket Sharma")
finally:
    file.close()
    
with open('uoutube.txt', 'w') as file:
    file.write(" Saket Sharma")