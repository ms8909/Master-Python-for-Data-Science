print("Enter Two numbers")

num1 = int(input())
num2 = int(input())

print("Enter your operator")

operator = input()

if operator == "+":
       sum = num1 + num2
       print(sum)
elif operator == "-":
        print(num1 - num2)
elif operator == "*":
        print(num1 * num2)
elif operator == "/":
        print(num1 / num2)
else:
    print("The operator is invalid")                        