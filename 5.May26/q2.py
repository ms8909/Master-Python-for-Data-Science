str1 = input("Enter 'True' or 'False' : ")
str2 = input("Enter 'True' or 'False' : ")

if (str1 == 'True' or str1 == 'False') and (str2 == 'True' or str2 == 'False'):
    if str1 == 'True' and str2 == 'True':
        output = False
    elif str1 == 'False' and str2 == 'False':
        output = False
    elif (str1 == 'True' and str2 == 'False') or (str2 == 'True' and str1 == 'False'):
        output = True
    print("XOR Result : ",output)
else:
    print("The inputs are not booleans,Please try again")