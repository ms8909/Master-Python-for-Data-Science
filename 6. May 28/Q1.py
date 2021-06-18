def Change_Data_Structure(names, age):

    people = []

    for i in range(len(names)):

        dic_name =names[i]
        dic_age = age[i]

        dic = {"names":dic_name, "age":dic_age}
        people.append(dic)

    print(people)

names= ["alan", "john", "tania", "ahmad", "ali", "muddassar", "raheel", "hamza"]
age= [12,13,14,15,17,16,13,13]

Change_Data_Structure(names, age)