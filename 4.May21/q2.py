def rectangle(l,b):
    for i in range(l):
        for j in range(b):
            print("*",end="")
        print("")    

print("How long is your flag - ",end="")
flagLen = int(input())
print("How wide is your flag - ",end="")
flagwid = int(input())
print("How long is your flagpole - ",end="")
flagpoleLen = int(input())
print("How wide is your flagpole - ",end="")
flagpolewid = int(input())

rectangle(flagLen,flagwid)
rectangle(flagpoleLen,flagpolewid)