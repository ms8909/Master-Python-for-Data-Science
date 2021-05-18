#THIS CODE CODED BY NAVEED TARIQ -> GITHUB: @naveid19


print("Enter the total number of classes held")
Classes_held = int(input())
print("Enter the number of classes attended by student")
Classes_attended = int(input())

#Farmula for attendence percentage
attendence_percentage = (Classes_attended/Classes_held) * 100

#converting float into string type
str_attendence_percentage = str(attendence_percentage)

#printing percentage of class attendence
print( "Student class attendence is " + str_attendence_percentage + "%")

#Allowed or not
if attendence_percentage> 75 :
    print("Student is allowed to sit in exam")

else: 
    print("Student is not allowed to sit in exam")