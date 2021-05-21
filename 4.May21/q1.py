# The Collatz Conjecture

def CollatzChain(no):
    while no!=1:
        print(no,end= " - ")
        if(no%2==1):
             no=(no*3)+1
        elif(no%2==0):
            no=int(no/2)
    print(no)

no=int(input("Enter A Number: "))
CollatzChain(no)
