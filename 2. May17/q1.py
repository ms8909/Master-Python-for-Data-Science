a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
print("What operation do you want to perform on these numbers")
c = input()

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)    
elif c == "/":
    print(a/b)
elif c == "%":
    print(a%b)    
else :
    print("Wrong inputs")