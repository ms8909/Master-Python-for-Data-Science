longflag = int(input("How Long is your Flag: "))
wideflag = int(input("How Wide is your Flag: "))
longflagpole = int(input("How Long is your Flagpole: "))
wideflagpole = int(input("How Long is your Flagpole: "))

def flag (length , width):
    for i in range(length):
        for j in range(width):
            print("*", end="")
        print()

def flagpole (length , width):
    for i in range(length):
        for j in range(width):
            print("*", end="")
        print()

flag(longflag , wideflag)
flagpole(longflagpole, wideflagpole)