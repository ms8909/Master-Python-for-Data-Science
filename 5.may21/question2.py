def printRec(l,b):
    for i in range(l):
        for j in range(b):
            print("*"*b, end="")
        print("")



print("how long is your flag? " , end="")

x  = int(input())

print("")

print("how wide is your flag? " , end="")

y  = int(input())

print("")

print("how long is your flagpole? " , end="")

xx  = int(input())

print("")

print("how wide is your flagpole? " , end="")

yy  = int(input())

print("")


printRec(x,y)
printRec(xx,yy)
