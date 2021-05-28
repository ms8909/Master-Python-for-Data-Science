print("Enter any positive integer")
x=int(input())
def is_prime(a):
    default= True
    for i in range(2,a):
        if a%i==0:
            default = False
    return(default)       
def factors(b):
    factors_list=[]
    for i in range(1,b+1):
        if b%i==0:
            factors_list.append(i)
    return(factors_list)        
def prime_factors(c):
    prime_factors_list=[]
    for i in range(1,len(c)):
        if is_prime(c[i])==True:
            prime_factors_list.append(c[i])
    return(prime_factors_list)        
is_prime(x)    
a=factors(x)
print("factors: ",)
print(a)
print("prime factors")
print(prime_factors(a))