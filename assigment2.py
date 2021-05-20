n = int(input("enter the number:"))
result = 1
for x in range (n,0,-1):
    result = result*x
    print("factorial of",n,"is",result)