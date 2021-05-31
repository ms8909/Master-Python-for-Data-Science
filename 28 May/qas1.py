name= ["alan","john" "tania", "ahmad", "ali", "muddassar", "raheel","hamza"]
age= [12,13,14,15,17,16,13,13]
people=[]
def funtion1(name,age):
    for a in range(7):
        j={}
        j.update({"names": name[a]})
        j.update({"age": age[a]})
        people.append(j)
        print(people)
funtion1(name,age)