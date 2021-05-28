names=["alam","jhon","taniya","ahmad","ali","muddassar","raheel","hamza"]
age=[12,13,14,15,17,16,13,13]
students=[]
for i in range(8):
    thisdict = {"name":names[i],"age": age[i],}
    students.insert(i,thisdict)
print("Peoples = ",students)
