a = input("Enter True or False")
b = input("Enter True or False")
if a=='True':
    a = True
elif a=='false':
    a=False
else:
    print("Inavlid value")

if b=='True':
    b = True
elif b =='false':
    b=False
else:
    print("Inavlid value") 


if a==True & b==True:
    print("XOR Result: False")
if a==True & b==False:
    print("XOR Result: True")
if a==False & b==True:
    print("XOR Result: True")
if a==False & b==False:
    print("XOR Result: False")