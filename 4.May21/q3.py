import random

def rollDice(num):
    luckyCounter=0
    for i in range(num):
        no1=random.randint(1,6)
        no2=random.randint(1,6)
        sum=no1+no2
        print("(",no1,",",no2,")")
        print("Dice Roll ",i+1," sum : ",sum)
        if sum==7:
            luckyCounter+=1
    return luckyCounter

print("How any times would you like to roll the Dice ? - ",end="")
roll=int(input())
print()
luckyCheck=rollDice(roll)

if luckyCheck>0:
    print("\nYou rolled Lucky seven ",luckyCheck," times")
else:
    print("\nOops!You didnt get lucky enough")