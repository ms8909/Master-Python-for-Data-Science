# Selection sort

list1=[1,5,67,2,43]
for i in range(len(list1)):
    for j in range(i,len(list1)):
        if list1[j]<list1[i]:
            abc=list1[i]
            list1[i]=list1[j]
            list1[j]=abc
print(list1)