names= ["alan","john", "tania", "ahmad", "ali", "mudassar", "raheel", "hamza"]
age= [12,13,14,15,17,16,13,13]
people=[]


for i in range(len(names)):
    people.append({"names": names [i], "Age" : age [i]}) 
    print("people =",people)

