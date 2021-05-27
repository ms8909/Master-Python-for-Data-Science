# The Collatz Conjecture

<<<<<<< HEAD
#Funtion:
=======

>>>>>>> 9b910ecb4ad76dbb47c1c6dbcf4572fd2bc77cc1
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
<<<<<<< HEAD

#Funtion's Call To Receive Length of Chain in Variable x.
x=CollatzChain(no)

print("Chain's Lenght: ",x)
=======
x=CollatzChain(no)
print("Chain's Lenght: ",x)
>>>>>>> 9b910ecb4ad76dbb47c1c6dbcf4572fd2bc77cc1
