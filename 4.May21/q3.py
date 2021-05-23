import random

def draw(chances):

    luck = 0

    minValue = 1
    maxValue = 6

    for i in range(chances):

        firstno = random.randint(minValue , maxValue)
        secondno = random.randint(minValue , maxValue)

        print("Your First Number is:",firstno , "Your Second Number is:", secondno, ", Which Equals: ",firstno + secondno)

        if firstno + secondno == 7:
            luck = luck + 1
            print("Congragulations! You've hit the Lucky 7")
        
        else:
            print("You might get lucky next time.")
        
    print("You had Your Luck:",luck ,"Time(s)")


chances = int(input("How many times would you Roll the Dice: "))
draw(chances)
