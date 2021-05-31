a=input("enter your number")
b=int(input("enter your number"))
for i in range(len(a)):
    ch=(ord(a[i]))+b
    print(chr(ch))