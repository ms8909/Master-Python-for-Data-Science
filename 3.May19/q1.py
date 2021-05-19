#Calculate Fictorial


def calFic(x):
    Fic=1
    if x==1 or x==0:
        return Fic
    while x>1:
        Fic*=x
        x-=1
    return Fic



print("Please enter the number")
Number = int(input())

Result = calFic(Number)

print("The result of ", Number, " fictorial is= ", Result)





