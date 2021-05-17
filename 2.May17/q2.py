print("Please enter the total number of classes")

NoC = int(input())

print("Please enter the number of classes you attended")

Att = int(input())


Perc = (Att/NoC)*100

print("Your attendance is ", Perc , "%")

if(Perc>=75):
    print("You are allowed to sit in the exam")
else:
    print("You are not allowed to sit in the exam")