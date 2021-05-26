# ARHAM RUMI

# Program to perform XOR operation

# Problem Statement

# --------------------------------------------------------------------------------------
# We’ve learned about the NOT, AND and OR logical operators in Python. Similarly, XOR is a binary operator that works on two Boolean values and returns True only if both of its operands differ and False otherwise. 

# Write a program that asks the user for two Boolean inputs and then prints the result of the XOR operation without usisng bitwise xor operator.
# --------------------------------------------------------------------------------------

print("\r")
print("Enter Two values to perform XOR on them")
print("\r")

def string_to_bool(s):
    bool_flag = True
    if s == "False":
        bool_flag = False
    elif s == "True":
        bool_flag = True
    else:
        print("Invalid Input")
    return bool_flag


def xor_operation(bool1, bool2):
    xor_status = True
    if bool1 == bool2:
        xor_status = False
        print(f"XOR Operation Output : {xor_status} ")
    else:
        print(f"XOR Operation Output : {xor_status} ")


userString1 = input(f"Enter ""True"" or ""False""  : ")
userString2 = input(f"Enter ""True"" or ""False""  : ")

userStr_1_status = string_to_bool(userString1)
userStr_2_status = string_to_bool(userString2)

xor_operation(userStr_1_status, userStr_2_status)