 #calculator    
a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
c = (input("Enter operator"))
if c== "+":
    print(a+b)
elif c== "-":
    print(a-b)
elif c== "*":
    print(a*b)
elif c== "%":
    print(a%b)
elif c== "/":
    print(a/b)
else :
        print("invalid input")