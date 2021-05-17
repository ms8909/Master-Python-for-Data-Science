#Calculator

#Three Inputs
# 2 Numbers and One for Operator

print("Input the first number")
x = int(input())
print("Input the second number")
y = int(input())
print("Select the Operator")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplicatiom")
print("4 - Division")
op = int(input())
if op==1: #Additiom
    print("Addition of ", x , " and ", y, "is: ", x+y)
elif op==2: #Subtraction
    print("Subtraction of ", x , " and ", y, "is: ", x-y)
elif op==3: #Multiplication
    print("Multiplication of ", x , " and ", y, "is: ", x*y)
elif op==4: #Division
    if y==0: #For divisor being zero
        print("Division by 0 is not possible")
    else:
        print("Division of ", x , " and ", y, "is: ", x/y)
else: #Operator input not being 1-4
    print("Invalid Operator Input")
