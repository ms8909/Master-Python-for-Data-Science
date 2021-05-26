# The Collatz Conjecture

#Funtion:
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

#Input From User:
no=int(input("Enter A Number: "))

#Funtion's Call To Receive Length of Chain in Variable x.
x=CollatzChain(no)

print("Chain's Lenght: ",x)