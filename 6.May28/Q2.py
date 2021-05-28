name = []
age = []
phone_number = []
address = []
n = int(input("Details of how many students you want to enter: "))
for j in range(n):
    a = input("Name: ")
    name.append(a)
    b = int(input("Age: "))
    age.append(b)
    c = int(input("Phone Number: "))
    phone_number.append(c)
    d = input("Address: ")
    address.append(d)
student = []
for i in range(n):
    student.append({"Name": name[i],"Age": age[i],"Phone Number": phone_number[i],"Address": address[i]})
print("Final List Student = ",student)