

def flag(p,q,r,s):

    for i in range(p):

        print("*"*q)

    for g in range(r):

        print("*"*s)

flaglong=int(input("How long Is Your Flag: "))
flagwide=int(input("How wide Is Your Flag: "))

plong=int(input("How long Is Your Flag Pole: "))
pwide=int(input("How wide Is Your Flag POle: "))

flag(flaglong, flagwide, plong, pwide)