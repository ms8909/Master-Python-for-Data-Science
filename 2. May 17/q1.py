# Program to build a mini calculator

print("Please Enter Two Numbers")
num1 = int(input())
num2 = int(input())

print("Please Enter symbol of the operation you want to perform")
operation = input()

if operation == "+":
    print(f"The Sum of above numbers is : {num1 + num2}")
elif operation == "-":
    print(f"The Subtraction of above numbers (num1 - num2) is : {num1 - num2}")
elif operation == "*":
    print(f"The Multiplication of above numbers is : {num1 * num2}")
elif operation == "/":
    print(f"The Division of above numbers (num1 / num2) is : {num1 / num2}")
else:
    print("Invalid Operator")