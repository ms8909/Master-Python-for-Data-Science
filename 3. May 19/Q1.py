n= int(input("Enter the number of factorail:  "))
factorial = 1

for i in range (n, 0, -1):   
    factorial= factorial * i
print(factorial)