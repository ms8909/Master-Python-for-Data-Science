student_name=[]
student_age=[]
student_address=[]
student_phone=[]
cond="y"
while cond=="y":
    name=input("Enter Name: ")
    student_name.append(name)
    age=input("Enter Age: ")
    student_age.append(age)
    phone=input("Enter Phone No: ")
    student_phone.append(phone)
    address=input("Enter Address: ")
    student_address.append(address)

    print("Enter Y for continue and N for Close")
    cond=input()
   
    for i in range (len(student_name)):
        student_data.append({"Name":student_name[i],"Phone":student_phone[i],"Age":student_age[i],"Address":student_address[i]})
        print(student_data )