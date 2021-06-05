list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4]
for i in range(len(list1)):
    for j in range(i,len(list1)):
        if list1[i]>list1[j]:
            p=list1[i]
            list1[i]=list1[j]
            list1[j]=p
print(list1)