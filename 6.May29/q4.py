print("Enter the message")
m=input()
print("Enter the numeric offset")
o=int(input())
x=[]
y=[]
for i in range(len(m)):
    x.append(ord(m[i]))
for i in range(len(x)):
    x[i]=x[i]+o
    y.append(chr(x[i]))
z=""
for i in y:
     z=z+i
print("The encrypted message is",z)
