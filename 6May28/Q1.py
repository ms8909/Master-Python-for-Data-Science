#Change Data Structures

# This will convert parameter arrays entries into dictionary and
# will store that dictionary into array.
def Change_Data_Structure(a,b):
    people=[]
    for i in range(len(a)):
        dic={"Name":a[i],"Age":b[i]}
        people.insert(i,dic)
    return people

#Main Function
print()
Names=["Anser","Ayaan","Hashir"]
Ages=[21,15,16]
People=Change_Data_Structure(Names,Ages)
print("People=>",People)
print()