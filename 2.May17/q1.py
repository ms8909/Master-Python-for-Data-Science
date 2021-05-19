# CALCULATOR


no1= int(input("Enter First Integer:"))         # input function takes input from user and value will store in no1 and no2 resepectively
no2= int(input("Enter second Integer:"))



operation=input("Enter an any operator of these for Specific operation  +,-,*,/,% :" )                 # Here user Enter Operator

if operation== "+" :                 #Addition
  print(no1 + no2)

elif operation== "-" :               #SUBTRACTION
  print(no1 - no2)

elif operation== "*" :               #Multiplication
  print(no1 * no2)

elif operation== "/" :               #Subtraction
  print(no1 / no2)

elif operation== "%" :               #Modulo
  print(no1 %  no2)

else:
  print("input character is not recognized !")                           # if user input wrong operator


