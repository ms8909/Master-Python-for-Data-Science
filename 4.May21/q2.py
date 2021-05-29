def rectangle(a,b):
    for i in range(a):
        print("*"*b)
def pole(c,d):
    for i in range(c):
        print("*"*d)
FlagL=int(input("How long is your Flag : "))
Flagw=int(input("How width is your Flag : "))
FlagPL=int(input("How long is your Flagpole : "))
FlagPW=int(input("How width is your Flagpole : "))
rectangle(FlagL,Flagw)
pole(FlagPL,FlagPW)
