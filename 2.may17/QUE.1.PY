#PROGRAM TO PERFORM ANY OF THE OPERATION ON THE NUMBER

print("Enter First Number")
num1 = int(input())
print("Enter the Second Number")
num2 = int(input())

print("chose operators from following (+,-,/,*,%")
operator = input()

if operator == '+':
    print(" the sum of given number is ")
    print(num1+num2)

elif operator == '-':
    print(" the subtraction of given  number is ")
    print(num1-num2)

elif operator == '*':
    print(" the Multipliction of given number ")
    print(num1*num2)

elif operator == '/':
    print(" the division of given number")
    print(num1/num2)

else:
    print("invalid inputr")
