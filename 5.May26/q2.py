# print("Enter 'True' or  'False' ")
# a=bool(input())
# # print("Enter 'True' or  'False' ")
# b=bool(input())
# if a==0 and b == 0:
#     return True
#     print(xorgate1)
# else:
#     return false
# # else:
# #     print("XOR statement is 'true'")




#XOR 


def XOR():
    print("Enter 'True' or 'False':" , end="")
    first = bool(input())
    print("Enter 'True' or 'False':" , end="")
    second = bool(input())
    if first == 'True':
        if second == 'False':
            return True
        return False 
    else:
        if second == 'False':
            return True
        return False


result = XOR()

print("XOR Result", end="")

if result:
    print("True")
else:
    print("False")