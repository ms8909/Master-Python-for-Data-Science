import random
print("How many times the two dices should be rolled")
x=int(input())
count=0
for i in range(1,x+1):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dicesum=dice1+dice2
    print(dice1,dice2)
    print("Dice roll",i,"sum:",dicesum)
    if dicesum==7:
        count=count+1

print("You rolled lucky seven",count,"times")
