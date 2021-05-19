


customer1_name= "Fahad"

customer2_name="Ayesha"

Customer3_name= "Ahsan"

customer4_name= ""

# Data Structures : List OR array 

customers_list= ["Fahad", "Ayesha", "Ahsan",  "Ali", "Tanveer", "Tehreem","Tehreem"]

age_list= [13,15,16,19,10,14,11]

print(len(customers_list))


print(customers_list[3:])

customers_list[2] = "New Name"

print(customers_list)

for i in [0,1,2,3,4,5,6,7,8,9]:  # range(10)
    print(i)
    if i<5:
        customers_list.append("Abdul")
        print(customers_list)

    else:
        customers_list.append("Bilal")
        print(customers_list)




