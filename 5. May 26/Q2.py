def xor ():  # XOR function
    if input1 != input2 :
        print("XOR result is : ",t)

    elif input1==input2:
        print("XOR result is : ",f)

    return(t,f)

# taking inputs
input1 = input("Enter 'True' or 'False' : ")
input2 = input("Enter 'True' or 'False' : ")
#delcaring the bool in variables
t=bool (1)
f=bool (0)
#checking exceptions
if (input1== "False" and input2== "True") or (input2== "False" and input1 == "True"):
    xor()
elif (input1== "False" and input2== "False" ) or (input2== "True" and input1 == "True"):
    xor()
else:
    print("invalid input") 