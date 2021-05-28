names = []
ages = []
phone = []
addresses = []
N = 0
con = ""
while con != 'n':
    names.append(input("Name: "))
    ages.append(input("Age: "))
    phone.append(input("Phone: "))
    addresses.append(input("Address: "))
    con = input("Do you want to continue(y/n): ")
    if con == 'y':
        N = N + 1

final_list_students = []


def my_function(name, age, phone_no, address):
    for i in range(N + 1):
        j = {}
        j.update({"name": name[i]})
        j.update({"age": age[i]})
        j.update({"phone": phone_no[i]})
        j.update({"address": address[i]})
        final_list_students.append(j)
    print(final_list_students)


my_function(names, ages, phone, addresses)
