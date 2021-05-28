def values(Offset,Message):
    Shift=""
    for i in Message:
        a=ord(i)
        a=a+Offset
        a=chr(a)
        Shift=Shift+a
    return Shift
Offset=int(input("Numeric Offset: "))
m=input("Message: ")
massege1=values(Offset,m)
print("Shifted Message: ",massege1)