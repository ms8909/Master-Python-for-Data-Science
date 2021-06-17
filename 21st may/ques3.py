



import random

count=0

diceroll=int(input("How many times would you like to roll the dic : "))

for i in range(diceroll):

    no1 = random.randint(1,6)
    no2 = random.randint(1,6)
    tamp=(no1,no2)
    print(tamp)
    print("Dise roll sum is :")
    disesum=no1+no2
    print(disesum)
    print()
    if disesum==7:
        count=count+1

print("Your lucky no 7 are in these given times")
print(count) 