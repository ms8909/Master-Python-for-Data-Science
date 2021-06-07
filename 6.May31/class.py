list1= [1,2,3,5,5,1,1]

search =1 

indexno=0
required_indexno=[]
for element in list1:
    if element==search:
        print("Here is the match at index: ", indexno)
        required_indexno.append(indexno)
    indexno= indexno+1



####
print(required_indexno)

