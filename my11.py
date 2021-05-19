print("Enter two Vaues")

num1 = float(input())
num2 = float(input())

print("Enter Operator")
oper=input()

if oper=="+":
    print("add = ")
    print(num1+num2)
elif oper=="-":
    print("Sub = ")
    print(num1-num2)
elif oper=="*":
    print("Multiple = ")
    print(num1*num2)
elif oper=="/":
    print("Div = ")
    print(num1/num2)
else:
    print("wrong input")
