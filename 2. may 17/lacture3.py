print('Please enter first number')
first_number = int(input())
print ('please enter second number')
second_number = int(input())
print('Please enter Operator')
operator = input()

if operator == '+':
    print('The Sum of two numbers is')
    print (first_number+second_number)
elif operator == '-':
    print ('The difference of two numbers is')
    print (first_number-second_number)
elif operator == '*':
    print('Multiplication of two numbers is')
    print(first_number*second_number)
else :
    print ('Divison of two numbers is')
    print (first_number/second_number)