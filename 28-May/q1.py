names= ["alan", "john", "tania", "ahmad", "ali", "muddassar", "raheel", "Hamza"]
age= [12,13,14,15,17,16,13,13]
people=[]
for i in range(len(names)):
    people.append({"Name": names [i], "Age": age [i]})
print("People = ",people)