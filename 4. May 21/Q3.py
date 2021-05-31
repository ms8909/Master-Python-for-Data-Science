import random
def Dice(roll):
    Lucky_seven = 0
    #n= int(input("How many times would you like to roll the dice? - "))
    for i in range(roll):
        Dice_no1 = random.randint(1,6)
        Dice_no2 = random.randint(1,6)
        print("(",Dice_no1,",",Dice_no2,")")
        print("Dice roll ",i+1, " sum: ", Dice_no1 + Dice_no2)
        if Dice_no1 + Dice_no2 == 7:
            Lucky_seven = Lucky_seven +1
    print()
    print("==============================================")
    print("|||    You rolled lucky seven ",Lucky_seven, " time(s)  |||") 
    print("==============================================")
    return Dice_no1, Dice_no2

n= int(input("How many times would you like to roll the dice? - "))
Dice(n)
 #Dice_n = random.randint(1,6)
