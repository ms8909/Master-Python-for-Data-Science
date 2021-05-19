
#  Taking two inputs as an operand.......

a = float(input("Enter the first input:"))
b = float(input("Enter the Second input:"))

#  Taking input as an operator.......

c = (input("Enter the operator:"))

if (c == '+'):
    d = a+b
    print("The sum of a and b is as follows ")
    print(d)
elif (c == '-'):
    d = a-b
    print("The subtraction  of a and b is as follows ")
    print(d)
elif (c == '*'):
    d = a*b
    print("The multiplication of a and b is as follows ")
    print(d)
elif (c == '/'):
    d = a/b
    print("The division of a and b is as follows ")
    print(d)
elif (c == '%'):
    d = a % b
    print("The modulus of a and b is as follows ")
    print(d)
else:
    print("Invalid Input.....")
