# Factorial
x=1
print("Enter the number to find it's factorial")
n=int(input())
for i in range(1,n):
    x*=(i+1)
print(x)