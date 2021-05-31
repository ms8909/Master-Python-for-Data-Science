# Lucky 7 In Ludo


def RollOn(a):
    lucky=0
    for x in range(a):
        import random
        no1=random.randint(1,6)
        no2=random.randint(1,6)

        print("(",no1,",",no2,")")

        sum=no1+no2
        print("Dice Roll ",x+1," Sum: ",sum)
        if(sum==7):
            lucky+=1
    return lucky



No=int(input("How Many Times Would YYou Like To Roll The Dices ? : "))
x=RollOn(No)
print("You Rolled Lucky 7 ",x," time(s)!")