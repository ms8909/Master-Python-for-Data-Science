s_name=[]
s_age =[]
s_phone =[]
s_adress =[]
cond = "Y"
while cond=="Y":
    name = input("Enter Sudent name")
    s_name.append(name)
    age = input("Enter student age")
    s_age.append(age)
    phone = input("Enter Student Phone Number")
    s_phone.append(phone)
    adress= input("Enter Student address")
    s_adress.append(adress)
    print("Enter y for continue and N for close")
    cond=input()
student_data =[]
for i in range (len(s_name)):
    student_data.append({"name": s_name[i], "age": s_age[i], "phone":s_phone[i], "adress": s_adress[i]})
print(student_data)