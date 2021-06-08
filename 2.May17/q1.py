#Calculator

print("Number 1:")
x=input()
print("Number 2:")
y=input()
x=int(x)
y=int(y)
print("Which Operation You Wanna Do ?")
c=input()
if c=="+":
    print(x+y)
elif c=="-":
    print(x-y)
elif c=="*":
    print(x*y)
elif c=="/":
    print(x/y)
elif c=="%":
    print(x%y)