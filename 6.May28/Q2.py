s_name=[]
s_age=[]
s_phone=[]
s_adress=[]
cond="Y"
while cond=="Y":
    name=input("Enter name of Student: ")
    s_name.append(name)
    age=input("Enter age of Student: ")
    s_age.append(age)
    phone=input("Enter phone number of Student: ")
    s_phone.append(phone)
    adress=input("Enter adress of Student: ")
    s_adress.append(adress)
    print("enter Y for continue or N for close: ")
    cond=input()
students_data=[]
for i in range(len(s_name)):
    students_data.append({"name": s_name[i], "age":s_age[i],"Phone": s_phone[i],"adress": s_adress[i]})
print(students_data)

