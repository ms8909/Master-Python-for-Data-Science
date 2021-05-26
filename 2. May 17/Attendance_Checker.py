# ARHAM RUMI

# Program to check attendance

# Problem Statement

# --------------------------------------------------------------------------------------
# student will not be allowed to sit in an exam if his/her attendance is less than 75%.
# Write a program that takes the following input from a user
# ● Number of classes held
# ● Number of classes attended.
# And prints
# ● percentage of class attended
# ● If a student is allowed to sit in the exam or not.
# --------------------------------------------------------------------------------------


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