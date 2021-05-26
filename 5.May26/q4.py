import math
def Factors(x):
    print("Factors of the given number is : ")
    for i in range(1,x+1):
        if x % i==0:
            print(i)

def primeFactors(n):
    print("Prime factors of the given number is : ")
    while n % 2 == 0:
        print (2)
        n = n / 2
         
    for i in range(3,int(math.sqrt(n))+1,2):
         
        while n % i== 0:
            print (i)
            n = n / i
             
    if n > 2:
        print (n)

def is_prime(n1):
    print("True for prime number and false for not a prime number : ")
    if n1==1:
        return False
    elif (n1==2):
        return True;
    else:
        for x in range(2,n1):
            if(n1 % x==0):
                return False
        return True              
y=input("Enter the number : ")
y=int(y)
a=print(is_prime(y))
Factors(y)
primeFactors(y)
