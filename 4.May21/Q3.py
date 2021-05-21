import random
x=int(input("How many times the two dices should be rolled"))
print(x)

count=0
for i in range(x):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dicesum=dice1+dice2
    print(dice1,dice2)
    print("Dice roll",i,"sum:",dicesum)
    if dicesum==7:
        count=count+1

print("You rolled lucky seven",count,"times")
