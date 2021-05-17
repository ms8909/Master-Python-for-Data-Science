# Mini Calculator

print("Enter The 1st Number")
num1 = int(input())

print("Please Enter the Desired Operator")
symbol = input()

print("Enter The 2nd Number")
num2 = int(input())

print("Your given statement is:", num1 , symbol , num2)

if symbol == "+":
    print(f"The sum of Your given Numbers is: {num1 + num2}")

elif symbol == "-":
    print(f"The Difference of Your given Numbers is: {num1 - num2} ")

elif symbol == "*":
    print(f"The Multiplication of Your given Numbers is: {num1 * num2} ")

elif symbol == "/":
    print(f"The Division of Your given Numbers is: {num1 / num2} ")

else:
    print("Invalid Operator")

