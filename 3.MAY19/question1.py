#program to find factorial of any number.
print("enter the number")
num= int(input())

factorial=1
for i in range(1,num + 1):
    factorial=factorial*i
   
print("factorial of number",num,"is")
print(factorial)