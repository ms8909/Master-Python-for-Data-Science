import random
x = int(input("How many times would you like to roll the dice? - "))
lucky = 0
for i in range(x):
    x = random.randint(1,6)
    y = random.randint(1,6)
    t = (x,y)
    print(t)
    z = x+y
    print("Dice roll",i,"sum:",z)
    if z == 7:
        lucky = lucky + 1
print("You rolled lucky seven",lucky,"times")