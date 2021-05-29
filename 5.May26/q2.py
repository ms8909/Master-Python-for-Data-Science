strinput1=input(str("Enter 'True' or 'False' : "))
strinput2=input(str("Enter 'True' or 'False' : "))
if strinput1=='True' and strinput2=='True':
   print("XOR Result: False")      
if strinput1=='False' and strinput2=='False':
    print("XOR Result: False")     
if strinput1!='False' and strinput2=='False':
    print("XOR Result: True")   
if strinput1=='False' and strinput2=='True':
    print("XOR Result: True")   