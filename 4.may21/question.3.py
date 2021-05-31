import random



def diceroll(NoT):
    LUCKY = 0
    for i in range(NoT):
        x = random.randint(1,6)
        y = random.randint(1,6)
        tu = (x,y)
        print(tu)
        print("Dice roll" , i+1 , "sum:", x+y)
        if x+y==7:
            LUCKY= lucky + 1
    print("You rolled lucky seven", LUCKY, "time(s)!")


#main

print("How many time would you like to roll the dice? ", end="")

x = int(input())

#calling function

diceroll(x)