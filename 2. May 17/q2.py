# Program to check attendance

name = input("Enter your name : ")
print(f"Hi {name}! fill up the following info to sit in exam")
print("")

classesHeld = int(input("How many classes are held overall : "))
classesAttended = int(input("How many classes have you attended : "))

classesPercentage = (classesAttended / classesHeld) * 100

print(f"Dear {name}! You have attended {classesPercentage}% classes")
print("")

if classesPercentage < 75:
    print(f"Dear {name}! Your attendance is less than 75%. So, you are NOT ALLOWED to sit in the exam")
else:
    print("Congratulations! You are ALLOWED to sit in the exam")