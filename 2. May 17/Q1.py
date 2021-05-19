num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
opr=input("Enter operator: ")
if opr=="+":
   print("Sum is:", (num1+num2))
elif opr=="-":
   print("sub is:", (num1-num2))
elif opr=="/":
   print("Division is:", (num1/num2))
elif opr=="*":
   print("Mul is:", (num1*num2))
else:
    print("wrong operatpr")