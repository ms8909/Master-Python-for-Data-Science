m = input("Enter your message: ")
o = int(input("Enter numeric offset: "))

for i in range(len(m)):
    ch = ord(m[i]) + o
    print(chr(ch),end="")

