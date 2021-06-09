def Insertion_Sort(list1):
    for i in range(1,len(list1)):
        temp = list1[i]
        j = i
        while j>0 and list1[j-1]>temp:
            list1[j] = list1[j-1]
            j = j-1
        list1[j] = temp
    return  list1
list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4]
print(Insertion_Sort(list1))