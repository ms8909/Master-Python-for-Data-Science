#Collatz Conjecture



def CollatzConjec(x):
    listt = [x]
    if x==1:
        return listt
    while x>1:
        if x%2==0:
            x=int(x/2)
            listt.append(x)
        else:
            x = int((3*x)+1)
            listt.append(x)
    return listt


print("Please enter a number to run Collatz Conjecture:" , end="")

y = int(input())

Result = CollatzConjec(y)

print()

print("The collatz chain is: ", end="")


l = len(Result)

for i in range(l):
    print(Result[i], end="")
    if(i<l-1):
        print(" - ", end="")


print()

print("Collatz chain length:", l)




