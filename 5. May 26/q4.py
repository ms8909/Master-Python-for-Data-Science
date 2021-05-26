# ARHAM RUMI

# Program to perform factorization of numbers

# Problem Statement

# --------------------------------------------------------------------------------------
# Tania is obsessed with factorizing numbers. She is in need of a module that has three functions:

# is_prime(n) takes an integer argument n and returns True if it is a prime number. It returns False if it is not. A prime number is any number that is only divisible by the numbers 1 and itself (EG: 7 and 13 are prime numbers). 1 is not a prime number.

# factors(n) takes an integer argument n and returns a list of all of its factors, that is, numbers which exactly divide n and leave no remainder (this includes 1 and n itself).

# prime_factors(n) takes an integer argument n and returns a list of all of its prime factors, that is, the factors which are prime numbers. This function should make use of the is_prime() and factors() functions specified above.

# Your job is to implement these functions and write the module. 
# --------------------------------------------------------------------------------------

print("\r")
print("Enter a Number to get factorization of it in different aspects ")
print("\r")

def is_prime(n):

    bool_flag = False

    if n > 1:  
        for i in range(2,n):  
            if (n % i) == 0:
                bool_flag = False
                break
            else:
                bool_flag = True

    return bool_flag


def factors(n):
    factors_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors_list.append(i)
    return set(factors_list)

def prime_factors(n):

    prime_factors_list = []
    all_factors = list(factors(n))

    for i in all_factors:
        if is_prime(i) == True:
            prime_factors_list.append(i)
    
    return prime_factors_list


num = int(input(f"Enter an Integer : "))
print("\r")

prime_status = is_prime(num)
if prime_status == True:
    print(f" {num} is PRIME ")
    print("\r")
else:
    print(f" {num} is NOT PRIME ")
    print("\r")

print(f" {num} has the following FACTORS : {factors(num)}")
print("\r")

print(f" {num} has the following PRIME FACTORS : {prime_factors(num)}")
