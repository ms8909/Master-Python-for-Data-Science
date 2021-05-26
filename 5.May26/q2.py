#XOR 


def XOR():
    print("Enter 'True' or 'False':" , end="")
    first = input()
    print("Enter 'True' or 'False':" , end="")
    second = input()
    if first == 'True':
        if second == 'False':
            return True
        return False
    else:
        if second == 'False':
            return False
        return True


result = XOR()

print("XOR Result", end="")

if result:
    print("True")
else:
    print("False")

