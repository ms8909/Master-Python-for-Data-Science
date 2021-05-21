# Program to draw cude flag

def drawFlag(l, b):

    print("\r")

    for i in range(l):
        for j in range(b):
            print("*", end="")
        print("\r")

# Main code
flagLen = int(input("Enter the LENGTH of the flag : "))
flagBreadth = int(input("Enter the BREADTH of the flag : "))
flagPoleLen = int(input("Enter the LENGTH of the flag pole : "))
flagPoleBreadth = int(input("Enter the BREADTH of the flag pole : "))

drawFlag(flagLen, flagBreadth)
drawFlag(flagPoleLen, flagPoleBreadth)