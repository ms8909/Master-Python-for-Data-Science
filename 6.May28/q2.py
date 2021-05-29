print("Enter the total number of students")
x=int(input())
final_list_students=[]

for i in range(x):
    a=input("Name")
    b=input("Age")
    c=input("Phone number")
    d=input("Address")
    dict= {"Name": a, "Age": b, "Phone number": c, "Address": d}
    final_list_students.append(dict)
print(final_list_students)


