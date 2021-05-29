# print("Enter a numebr")
# number=int(input())
# print(number)
def is_prime(n):
    count = 0
    for item in range(2,n):
        if  n%item==0:
            count=1
            return "false"
        elif count==0:
            return "true"

print(" Enter a number ")
n=int(input())

print(is_prime(n))

number=42
count=0;
print("Factors of given number are")
for item in range(1,number+1):
    factor=number%item
    if factor==0:
        print(item)
count=0
for i in range(2,item):
    if  is_prime(item):
        print(i)



      
    





