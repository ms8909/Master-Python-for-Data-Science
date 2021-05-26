# ARHAM RUMI

# Program to print Average and Product of all the entered numbers

# Problem Statement

# --------------------------------------------------------------------------------------
# Write a program that takes integer inputs from the user until 
# he/she presses q ( Ask to press q to quit after every integer input ). 
# Print average and product of all numbers.
# --------------------------------------------------------------------------------------


print("Enter the integers to get their Average and Product")
print("Enter q to Quit")

sum = 0
product = 1
avg = 0

i = 1
while i:
    in_char = input()
    if(in_char == 'q'):
        break
    else:
        num = int(in_char)
        product *= num
        sum += num
        i += 1

avg = sum / (i-1)

print(f"Product of all numbers is : {product} ")
print(f"Average of all numbers is : {avg} ")