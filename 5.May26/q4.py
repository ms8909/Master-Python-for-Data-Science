def factors(n):
    factors = []
    for i in range(1,n+1):
        if n%i==0:
            factors.insert(i,i)
    return factors

def is_prime(n):
    temp = 0
    if n==1 or n==0:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                temp = temp + 1
        if temp > 0:
            return False
        else:
            return n

def prime_factors(n):
    prime_factors = []
    fac = factors(n)
    print("Factors are: ",fac)
    for n in range(0,len(fac)):
        if is_prime(fac[n])!=False:
            prime_factors .insert(0, is_prime(fac[n]))
    print("Prime Factors are: ",prime_factors [::-1])

n = int(input("Enter any number: "))
prime_factors(n)