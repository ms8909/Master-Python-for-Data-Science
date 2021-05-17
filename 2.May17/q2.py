print("Enter total number of classes")
totalClasses = int(input())
print("Enter number of classes attended")
attendedClasses = int(input())

percentage = (attendedClasses / totalClasses) * 100
print("Student has "+str(percentage)+" attendace")
if percentage<75:
    print("Student is not allowed to sit in exam")
else:
    print("Student is allowed to sit in exam")    