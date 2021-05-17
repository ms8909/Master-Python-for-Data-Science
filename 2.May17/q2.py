# Attendance Checker

print("Please Calculate Your Attendance")
print(" ")

attend = int(input("Total Number of Classes Attended are: "))
held = int(input("Total Number of Classes Held are: "))

print(" ")

percentage = (attend / held) * 100

print (f"you have attended {percentage}% classes")
print(" ")

if percentage < 75:
    print("You are not Allowed to Sit in Exam.")

else:
    print("Congragulations! You are Allowed to Sit in Exam.")