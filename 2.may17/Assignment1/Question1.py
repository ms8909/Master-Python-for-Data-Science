
#program to perform any of the operation on two number(+,-,/,*,%)

print("Enter First Number")
num1 = int(input())
print("Enter The Second Number")
num2 = int (input())

print("Choose Opertors from following  (+,-,/,*%)")
operator = input()

if operator == '+':
    print (" The sum of given numbers is ")
    print(num1+num2)

    
elif operator == '-':
    print (" The Subtraction of given numbers is ")
    print(num1-num2)

    
elif operator == '*':
    print (" The Multiplication of given numbers is ")
    print(num1*num2)

    
elif operator == '/':
    print (" The Division of given numbers is ")
    print(num1/num2)

    
elif operator == '%':
    print (" The Modulus of given numbers is ")
    print(num1%num2)

else:
    print("Invalid Input")

