flaghight=int(input("enter hight of the flag"))
flagwidth=int(input("enter flag width"))
polehight=int(input("enter pole hight"))
polewidth=int(input("enter pole width"))
def flagmaking(flaghight,flagwidth,polehight,polewidth):
    for i in range(flaghight):
        for j in range(flagwidth):
            print("*",end="")
        print()
    for i in range(polehight):
        for j in range(polewidth):
            print("*",end="")
        print()

flagmaking(flaghight,flagwidth,polehight,polewidth) 
