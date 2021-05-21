# Program to get Lucky 7 in LUDO

import random


def diceRoll(count):

    luckyRolls = 0

    for i in range(count):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        diceRolledTuple = (dice1, dice2)
        diceTotal = sum(diceRolledTuple)

        print(f"Dice roll {count} sum is : {diceTotal} ")

        if diceTotal == 7:
            luckyRolls += 1
        
    print("\r")
    print(f"Your Lucky 7 Rolls are : {luckyRolls} ")


print("--------------------------------------------------------------------------------------")
print("There are Two dices in the game. Let's see how many times do you get the lcuky 7 total")
print("--------------------------------------------------------------------------------------")

diceRollingCount = int(input("How many times do you want to roll the dice : "))
print("\r")

diceRoll(diceRollingCount)