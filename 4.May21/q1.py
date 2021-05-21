# The Collatz Conjecture


def CollatzChain(no):
    lenght=0
    while no!=1:
        print(no,end= " - ")
        lenght=lenght+1
        if(no%2==1):
             no=(no*3)+1
        elif(no%2==0):
            no=int(no/2)
    print(no)
    lenght=lenght+1
    return lenght

no=int(input("Enter A Number: "))
x=CollatzChain(no)
print("Chain's Lenght: ",x)
