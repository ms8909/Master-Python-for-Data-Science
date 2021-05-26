def is_prime(n):
    prime=True
    if n==1:
        prime=False
    else:   
        for i in range(2,(n//2)+1):
            if n%i==0:
                prime=False
                break
    return prime 

def factors(n):
    li=[]
    for i in range(1,n+1):
        if n%i==0:
            li.append(i)
    return li       

def prime_factors(n):
    li=[]
    for i in n:
        if is_prime(i)==True:
            li.append(i)
    return li

n=int(input("Enter a number"))
f=factors(n)
print("Factors(",n,") : ",end="")
print(f)
print("Prime_Factors(",n,") : ",end="")
print(prime_factors(f))       