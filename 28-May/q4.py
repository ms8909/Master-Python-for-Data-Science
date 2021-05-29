m=input("Enter Messege: ")
o=int(input("Enter Numeric Ofset: "))
for i in range(len(m)):
    ch=  ord(m[i])+o
    print(chr(ch),end="")
    #print(ord(m[i]))
