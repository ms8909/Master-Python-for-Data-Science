# ARHAM RUMI

# Program to print the following pattern

# Problem Statement

# --------------------------------------------------------------------------------------
# Print the following patterns using loop
# --------------------------------------------------------------------------------------

# *
# **
# ***
# ****

print("Printing Pattern A")
print("")

for i in range(4):
    for j in range(0, i+1):
        print("*" , end="")
    print("\r")

# -----------------------------------------
print("-----------------------------------")
# Program to print the following pattern

#   *  
#  *** 
# *****
#  *** 
#   *  

print("Printing Pattern B")
print("")


for i in range(3):
    print(" "*(3-i), "*"*(i*2+1))
for j in range(3-2, -1, -1):
    print(" "*(3-j), "*"*(j*2+1))

# -----------------------------------------
print("-----------------------------------")
# Program to print the following pattern

# 1010101
#  10101 
#   101  
#    1   

print("Printing Pattern C")
print("")
num=7

for i in range((num // 2) + 1, num+1):
    for j in range(i - (num // 2) + 1):
        print(" ", end="")
    for k in range(1, ((num+1-i) * 2-1) +1):        
        print(k % 2, end="")
    print("")