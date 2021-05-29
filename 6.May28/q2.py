def values(no):
    students=[]
    for i in range(data):
        print()
        print("Enter Student",i+1,"name : ")
        names=input()
        print("Enter Student",i+1,"age : ")
        age=int(input())
        print("Enter Student",i+1,"phone no : ")
        phone_no=int(input())
        print("Enter Student",i+1,"address : ")
        address=input()
        dict = {i+1:{"name":names,"age": age,"phone no":phone_no,"address": address}}
        students.insert(i,dict)
    return students
data=int(input("enter the number of students you wanted to enter data : "))
List_Of_All_Students=values(data)
print("List Of All Students: ",List_Of_All_Students)
