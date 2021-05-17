print("Enter Ist the number")
a =int (input())



print("Enter 2nd number")
b= int(input())

c=input("Please select the operator \n")

print(" Results are ")
if c=="+":
    print(a+b)
elif c==("-"):
    print(a-b)
elif c==("*"):
    print(a*b)
elif c==("/"):
    print(a/b)


else:
    print("Wrong Symbol")    