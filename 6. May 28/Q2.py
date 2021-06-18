names= []
age= []
phone= []
address = []
final_list_students = []

num_of_students = int (input("Enter the number of student's data : "))

for i in range(num_of_students):

    name_of_student = input("Name : ")
    names.append(name_of_student)

    age_of_student = int (input("Age : "))
    age.append(age_of_student)

    phoneNum_of_student = int (input("Phone Number : "))
    phone.append(phoneNum_of_student)

    address_of_student = input("Address : ")
    address.append(address_of_student)
    if i != (num_of_students -1):
        print()
        print("Next student's data")
        print()

for i in range(num_of_students):

    dic_name =names[i]
    dic_age = age[i]
    dic_phone =phone[i]
    dic_address = address[i]

    dic = {"name":dic_name, "age":dic_age, "phone": dic_phone,"address": dic_address}
    final_list_students.append(dic)

print(final_list_students)