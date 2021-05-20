#Attendance checker
ClassesHeld=int(input("Enter Total Number Of Classes Held : "))
ClassesAttended=int(input("Enter Number Of Classes You Attended : "))

Answer=(ClassesAttended/ClassesHeld)*100

if Answer>=75:
    print("Your Attendance Percentage: ",Answer)
    print("You can sit for exams.")
elif Answer<75:
    print("Your Attendance Percentage: ",Answer)
    print("You can't sit for exams. Better Luck Next Time!!!")