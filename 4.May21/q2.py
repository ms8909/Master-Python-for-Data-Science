# Kenny's Flag

#Function:
def flag(a,b,c,d):
    for i in range(a):
        print("*"*b)
    for g in range(c):
        print("*"*d)


#To Take Inputs From User:
Flong=int(input("How Long Is Your Flag: "))
Fwide=int(input("How Wide Is Your Flag: "))

Plong=int(input("How Long Is Your FlagPole: "))
Pwide=int(input("How Wide Is Your FlagPole: "))

#Function's Call:
flag(Flong,Fwide,Plong,Pwide)
