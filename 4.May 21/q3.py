#Function
def Rollon(a):
    lucky=0
    min = 1
    max = 6
    for x in range(a):

        import random

        no1=random.randint(min,max)
        no2=random.randint(min,max)

        print("(",no1,",",no2,")")

        sum = min + max
        print("Dice roll ",x+1,"sum: ",sum)
        if (sum==7):
            lucky+=1

        return lucky

#Input From User:
No=int(input("How many times would you like to roll the dice ? : "))        

#Function's call to receive length of chain in variable x.
x=Rollon(No)

print("You rolled lucky 7 ",x,"time(s)!")




    


#Input from user:
#No=int(input()) 
