#program to find factorial of any number.

print("Enter the number")
num = int (input())


factorial=1
for i in range(1,num + 1 ):
    factorial=factorial*i
print("Factorial of number",num,"is " )
print(factorial)