#Python program to print a flag using star pattern

flaglength = int(input("How long is your flag?  : "))
flagwidth = int(input("How wide is your flag?  : "))
polelength =int(input("How long is your flagpole?  : "))
polewidth =int(input("How wide is your flagpole?  : "))

print("Flag Star Pattern") 
for i in range(flaglength):
    for j in range(flagwidth):
        print('*', end = '  ')
    print()

for i in range(polelength):
    for j in range(polewidth):
        print('*', end = '  ')
    print()