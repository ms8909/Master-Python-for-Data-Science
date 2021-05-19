def calculate():
    operation = input('''
  Please choose the operators which do you want to perform.!
  + for Addition
  - for Subtraction
  * for Multiplication
  / for Division
''')
    number_1 = int(input('Enter Your First Number'))
    number_2 = int(input('Enter Your Second Number'))
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operation == '-':
        print('{} - {} ='.format(number_1, number_2))
        print(number_1 - number_2)
    elif operation == '*':
        print('{} * {} ='.format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == '/':
        print('{} / {} ='.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print('You have attempet worng operations..Please Choose corect..!')
    again()

def again():
    doagain = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if doagain.upper() == 'Y':
        calculate()
    elif doagain.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()