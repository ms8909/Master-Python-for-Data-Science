def cipher(m,o):
    l=[]
    s=""
    for i in m:
        l.append(i)
    
    for i in range(len(l)):
        a=ord(l[i])
        a+=o
        b=chr(a)
        l[i]=b

    for i in l:
        s=s+i
    return s
# main

msg=input("Enter a message : ")
off=int(input("Enter an offset : "))
print()
print("The ciphered msg is : ",cipher(msg, off))