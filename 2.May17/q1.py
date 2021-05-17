num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))
operator=str(input("enter your operator:"))
if operator=='+':
    print("Addition of two numbers is:")
    print(num1+num2)
elif operator=='-':
    print("Subtraction of two numbers is:")
    print(num1-num2)
elif operator=='*':
    print("Multiplication of two numbers is:")
    print(num1*num2)
elif operator=='/':
    print("Division of two numbers is:")
    print (num1/num)
elif operator=='%':
    print("Reminder of two numbers is:")
    print (num1%num2)
else:
   print("wrong inputs")