m = input("Enter Message: ")
o = int(input("Enter offset: "))
def msg():
    for i in range(len(m)):
        c = ord(m[i]) + o
        print(chr(c),end="")
msg()