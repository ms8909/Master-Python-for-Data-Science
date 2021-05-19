# Attendence Chkecker

classes_Held=float(input("Enter Number of Held Classes:"))
Classes_Attend=float(input("Enter Number of Attend Classes:"))
percentage=(Classes_Attend/classes_Held *100)
print(percentage)


if (percentage<75):
    print("Student is not Allowed to sit in Exams because percentage of Student is")

elif(percentage>74):
   print("Student is Allowed to sit in Exams because percentage of Student is")

else:
    print("your input is invalid")
print(percentage)





    
