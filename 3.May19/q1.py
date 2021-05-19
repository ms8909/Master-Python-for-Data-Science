print("Enter any number to find its factorial = ",end="")
number = int(input())
factorial = 1
for i in range(1,number+1):
    factorial = i * factorial
print("The factorial of number = ", factorial)