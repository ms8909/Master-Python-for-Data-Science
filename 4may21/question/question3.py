import random
def draw(chances):
    luck = 0
    min = 1
    max = 6
    for i in range(chances):

        first=random.randint(min,max)
        second = random.randint(min,max)

        print("You 0entered First Number is:",first , "You Second Number is:", second, ", Which Equals: ",first + second)

        if first+second== 7:
            luck=luck+1
            print("Congragulations! You've hit the Lucky 7")
        
        else:
            print("You might get lucky next time.")
        
    print("You had Your Luck:",luck ,"Time(s)")


chances = int(input("How many times would you Roll the Dice: "))
draw(chances)
