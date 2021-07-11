def insertionSort(l):
    for i in range(1,len(l)):
        temp = l[i] 
        j=i-1 
        while j>=0 and l[j] > temp:
            l[j+1] = l[j]
            j=j-1 
        l[j+1]=temp
    return l    

list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
print(insertionSort(list1))
