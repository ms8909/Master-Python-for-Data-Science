print("To sit in the Exam the Student must have attendence percentage 75% or more than 75%") 
a = int(input("Enter Number of Classes held = "))
b = int(input("Enter Number of Classes attended = "))
c = (b/a)*100
print("The Attendence percentage of the student is = ",c)
if (c < 75):
    print("Student is not allowed to sit in the Exam")
elif (c >= 75):
    print("Student is allowed to sit in the Exam")    