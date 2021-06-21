def XOR(a,b):
    if(a=="True" and b=="False" or a=="False" and b=="True"):
        return True
    else:
        return False

# Main Function
a=input("Enter 'True' Or 'False' : ")
b=input("Enter 'True' Or 'False' : ")

print("XOR Result : ",XOR(a,b))