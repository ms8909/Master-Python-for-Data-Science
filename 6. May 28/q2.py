def convert_info(name, age, phone_num, address, list):
  list.append(
    {
      'Name': name,
      'Age': age,
      'Phone Number': phone_num,
      'Address': address
    }
  )

name = input('Please input your name: ')
age = int(input('Please input your age: '))
phone_num = input('Please input your phone number: ')
address = input('Please input your address: ')

final_list_students = []

convert_info(name, age, phone_num, address, final_list_students)

print(final_list_students)


