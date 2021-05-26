# ARHAM RUMI

# Program to calculate FACTORIAL of a number

# Problem Statement

# --------------------------------------------------------------------------------------
# Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n. E.g.-
# 4! = 1*2*3*4 = 24
# 3! = 3*2*1 = 6
# 2! = 2*1 = 2
# Also,
# 1! = 1
# 0! = 1

# Write a program to calculate the factorial of a number.
# --------------------------------------------------------------------------------------

num = int(input("Enter a number to get it's factorial: "))

fact = 1

if num == 0 or num == 1:
    fact = 1
else:
    for i in range(1, num+1):
        fact *= i

print(f"Factorial of {num} is : {fact}")