# ARHAM RUMI
# Program to get Lucky 7 in LUDO

# Problem Statement

# --------------------------------------------------------------------------------------
# Write a program that 
# Asks users to tell how many times the two LUDO six-sided dice should be rolled.
# Returns the result of a randomized roll of two six-sided dice. This means that two random 
# integer values between 1 and 6 (inclusive) need to be returned. 

# If the sum of two dies is 7, we call this a lucky event.

# Your program should 
# keep track of the number of times the sum of the two die turn out to be 7
# print out how many times this lucky event occurred. 
# --------------------------------------------------------------------------------------


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