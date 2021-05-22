# Collatz Conjecture


def Collcon(a):
    list = [a]
    if a == 1:
        return list
    while a > 1:
        if a % 2 == 0:
            a = int(a/2)
            list.append(a)
        else:
            a = int((3*a)+1)
            list.append(a)
    return list


print("Enter a number to run Collatz Conjecture:", end="")

b = int(input())

res = Collcon(b)

print()

print("The collatz chain is: ", end="")


l = len(res)

for i in range(l):
    print(res[i], end="")
    if(i < l-1):
        print(" - ", end="")


print()

print("Collatz chain length:", l)
