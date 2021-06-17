
# xor 
x=input("Enetr True or False: ")
y=input("Enetr True or False: ")
if x=='True':
    x=True
elif x=='False':
    x=False
else:
    print("invalid input")

if y=='True':
    y=True
elif y=='False':
    y=False
else:
    print("invalid input")

if x== True and y==True:
    print("XOR Result: False")
elif x==True and y==False:
    print("XOR Result: True")        
elif x==False and y==True:
    print("XOR Result: True")    
elif x==False and y==False:
    print("XOR Result: False") 