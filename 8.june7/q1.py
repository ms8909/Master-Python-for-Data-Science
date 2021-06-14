#Q no 1
def insertionsort(list):
    for i in range (1, len(list)):
        j=i-1
        while j>=0:
            if (list[i]<list[j]):
                P=list[j]
                list[j]= list[i]
                list[i]=P
                i-=1
        j=j-1   
    return list
list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
list1 = insertionsort(list1)
print(list1)