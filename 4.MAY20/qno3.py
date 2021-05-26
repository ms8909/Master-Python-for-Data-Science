#question no 3
import random


def luckysevens():
    mypot = int(input("Please enter the amount of money you want to in the pot: "))

    while mypot > 0:
        diceroll = random.randint(1, 6)
        print(diceroll)
        myroll = (diceroll + diceroll)
        if myroll == 7:
            mypot = mypot + 4
            print("Your roll was a 7 you earned 4$", mypot)
        else:
            mypot = mypot - 1
            print("Your roll was", myroll, "you lost 1$", mypot)
    if mypot == 0:
        print("Your out of money!")
    sum = 0
    for count in range(myroll + 1):
        sum = sum + count
    print(count)


luckysevens()