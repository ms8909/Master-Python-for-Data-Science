# Factors & Prime Factors

def is_prime(n):
    x=2
    while x<n :
        if(int(n%x==0)):
            return False
        x=x+1
    return True

def factors(n):
    x=1
    ans=[]
    while x<=n:
        if(n%x==0):
            ans.append(x)
        x+=1
    return ans

def prime_factors(n):
    Fac=factors(n)
    ans=[]
    for x in range(len(Fac)):
        if(is_prime(Fac[x])==True and Fac[x]!=1):
            ans.append(Fac[x])
    return ans


n=int(input("Enter a number to check it is prime , to get it's factors and prime factors: "))
print("Its Prime: ",is_prime(n))
print("No's Factors => ",factors(n))
print("No's Prime-Factors => ",prime_factors(n))