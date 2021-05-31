
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