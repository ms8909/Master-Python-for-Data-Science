# Number of classes held = noClassHeld
# Number of classes attended = noClassAttend
print("Enter number of classes held")
noClassHeld = int(input())
print("Enter number of classes attended")
noClassAttend = int(input())
percentage = (noClassAttend/noClassHeld)*100
print("Percentage of class attended = ", percentage)
if percentage < 75:
    print("Your are not allowed to sit in an exam because your attendance is less than 75%")
else:
    print("Your are allowed to sit in the exam")

