#Inut of classes

print("Please enter the total number of classes")

NoC = int(input())


#Input of atendance
print("Please enter the number of classes you attended")

Att = int(input())

#Calculating percentage
Perc = (Att/NoC)*100

#Printing Percentage
print("Your attendance is ", Perc , "%")

#Condition for permission
if(Perc>=75):
    print("You are allowed to sit in the exam")
else:
    print("You are not allowed to sit in the exam")
