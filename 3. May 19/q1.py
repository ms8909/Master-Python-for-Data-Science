# Program to calculate FACTORIAL of a number

num = int(input("Enter a number to get it's factorial: "))

fact = 1

if num == 0 or num == 1:
    fact = 1
else:
    for i in range(1, num+1):
        fact *= i

print(f"Factorial of {num} is : {fact}")