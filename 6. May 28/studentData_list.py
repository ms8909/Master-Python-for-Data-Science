# ARHAM RUMI

# Program to Saving Student's Data in the List

# Problem Statement

# --------------------------------------------------------------------------------------
# Write a program that asks a user to input the following details of ‘N’ number of students.

# Name 
# Age
# Phone number
# Address

# The program should save the data in the format like

# final_list_students= [ dict, dict, dict, ….., dictN ]

# Where each dict is {“name: “alan”, “age”: 12, “phonenumber”:0222233, “address”:”xyz street” }
# --------------------------------------------------------------------------------------

print("Enter the Students Data")
print("\r")
print("\r")
print("---------------------------------------------------------------------------")
print("NOTE: ----   PLEASE SEPARATE THE STUDENT'S ATTRIBUTES WITH ONE COMMA   ----")
print("---------------------------------------------------------------------------")
print("\r")
print("\r")


def studentsDictionary(numOfStudents):

    peopleList = []
    for i in range(0, numOfStudents):
        name, age, phone, address = input("Enter Name, Age, Phone Number, Address : ").split(",")
        age = int(age)
        phone = int(phone)
        peopleList.append({'Name': name, 'age': age, 'Phone': phone, 'Address': address})
    return peopleList



def printData(studentsDataList):
    for i in studentsDataList:
        print(i)
        print("\r")


students = int(input("Enter Number of Students for your Data : "))
print("\r")

studentsData = studentsDictionary(students)
print("\r")

printData(studentsData)