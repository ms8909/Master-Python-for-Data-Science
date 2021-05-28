def RollOn(a):
    lucky=0
    for x in range(a):
# Declaring the sequence
        import random
        no1=random.randit(1,6)
        no2=random.randit(1,6)

        print("(",no1,",",no2,")")

        sum=no1+no2
        print("Dice Throw",x+1,"Sum: ",sum)
        if(sum==7):
            lucky+=1
            
    return lucky 

#Input From User:
No=int(input("How Many Times Would You Like To Throw The Dices?  : "))

x=RollOn(No)
print("You Rolled Lucky 7",x,"time(s)!")