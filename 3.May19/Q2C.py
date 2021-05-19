def invert(n):
    if n ==1:
            return 0
    else:
        return 1
n = 1
linerange = 7
for a in range(4):
    print(" "*a, end="")
    for b in range(linerange):
        print(n,end="")
        n = invert(n)
    n = invert(n)
    linerange -=2
    print() 