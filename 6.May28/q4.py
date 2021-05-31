#Cyber Security


print("enter message:")
m = input()
print("enter offset")
o = int(input())



def encrypt(m,o):
    l = len(m)
    strr = ""
    for i in range(l):
        s = ord(m[i])
        s +=o
        strr = strr + chr(s)

    return strr





print(encrypt(m,o))
