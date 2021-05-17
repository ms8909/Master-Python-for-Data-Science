# Calculator
a = int(input("Enter first number = "))
b = int(input("Enter second number = "))
oper = input("Enter operator =")
if oper == '+':
    print("Result = ",a+b)
elif oper == '-':
    print("Result = ",a-b)
elif oper == '/':
    print("Result = ",a/b)
elif oper == '*':
    print("Result = ",a*b)
elif oper == '%':
    print("Result = ",a%b)
else:
    print('operator is not supported')
