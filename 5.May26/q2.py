print("Enter True or False")
x=input()
print("Enter True or False")
y=input()

if x=="True":
    x=True
elif x=="False":
    x=False
else:
    print("Only True and False inputs are valid")

if y=="True":
    y=True
elif y=="False":
    y=False
else:
    print("Only True and False inputs are valid")

if x== True and y==True:
 print("XOR Result: False")
elif x==True and y==False:
    print("XOR Result: True")        
elif x==False and y==True:
    print("XOR Result: True")    
elif x==False and y==False:
    print("XOR Result: False")
