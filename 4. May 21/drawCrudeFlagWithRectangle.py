# ARHAM RUMI

# Program to draw cude flag

# Problem Statement

# --------------------------------------------------------------------------------------
# Kenny likes rectangles so much that he decided to write a Python function rectangle(l,b) that,
# given a length and breadth as arguments, uses asterisks (“*”) to print out a simple rectangle on the screen.
# He then uses this function to draw a crude flag according to user-given specifications.
# Write a code to draw a crude flag to demonstrate rectangles 
# --------------------------------------------------------------------------------------


def rectangle(l, b):

    for i in range(l):
        for j in range(b):
            print("*", end="")
        print("\r")

# Main code
flagLen = int(input("Enter the LENGTH of the flag : "))
flagBreadth = int(input("Enter the BREADTH of the flag : "))

flagPoleLen = int(input("Enter the LENGTH of the flag pole : "))
flagPoleBreadth = int(input("Enter the BREADTH of the flag pole : "))

print("\r")
rectangle(flagLen, flagBreadth)
rectangle(flagPoleLen, flagPoleBreadth)