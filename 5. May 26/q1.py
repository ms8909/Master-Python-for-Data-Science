# ARHAM RUMI

# Program to print ASCII sum of a String

# Problem Statement

# --------------------------------------------------------------------------------------
# For this question, we’ll be working with strings and ASCII values. Here is a link to some information on ASCII values: http://www.computerhope.com/jargon/a/ascii.html

# Python supports two built-in functions, ord() – which converts a character to its integer ASCII value and chr() – which takes a given valid ASCII value and returns its character equivalent.

# You’ll need to define three functions: 

# ascii_sum(s) should calculate the sum of the ASCII values of ALL the characters in a given string ‘s’

# ascii_sum_odd(s) should calculate the sum of the ASCII values of all the ODD-numbered characters in a given string ‘s’

# ascii_sum_even(s) should calculate the sum of the ASCII values of all the EVEN-numbered characters in a given string ‘s’

# For example, the uppercase string ‘ABC’ has the following scores

# ABC = 198
# A+C = 132
# B = 66
# --------------------------------------------------------------------------------------

print("We will return you the ASCII sum of the String in different aspects")
print("\r")

def ascii_sum(s):
    sum = 0
    print("All Characters in the String with their respective ASCII values are -------")
    print("  Char ---->>> ASCII : ")
    print("\r")
    for i in s:
        char_ascii_val = ord(i)
        sum += char_ascii_val
        print(f"    {i}  ---->>>    {char_ascii_val}")
    
    print("\r")
    print(f"ASCII Sum of All Characters : {sum} ")

def ascii_sum_odd(s):
    sum = 0
    print("All Characters at OOD indexes in the String with their respective ASCII values are -------")
    print("  Char ---->>> ASCII : ")
    print("\r")
    for i in s:
        if (s.index(i) + 1) % 2 != 0:
            char_ascii_val = ord(i)
            sum += char_ascii_val
            print(f"    {i}  ---->>>    {char_ascii_val}")
    
    print("\r")
    print(f"ASCII Sum of Odd Characters : {sum} ")

def ascii_sum_even(s):
    sum = 0
    print("All Characters at EVEN indexes in the String with their respective ASCII values are -------")
    print("  Char ---->>> ASCII : ")
    print("\r")
    for i in s:
        if (s.index(i) + 1) % 2 == 0:
            char_ascii_val = ord(i)
            sum += char_ascii_val
            print(f"    {i}  ---->>>    {char_ascii_val}")
    
    print("\r")
    print(f"ASCII Sum of Even Characters : {sum} ")

userString = input(f"Enter a String : ")

ascii_sum(userString)
ascii_sum_odd(userString)
ascii_sum_even(userString)