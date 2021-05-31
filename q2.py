def flag(a,b,c,d):
    for i in range(a):
        print("*"*b)
    for g in range(c):
        print("*"*d)


Flong= int(input(" How Long Is Your Flag :"))      
Fwide=int(input("How Wide is your Flag:"))

Plong= int(input(" How Long Is Your FlagPole :"))      
Pwide=int(input("How Wide is your FlagPole:"))
flag(Flong,Fwide,Plong,Pwide)

