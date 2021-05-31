def bubbleSort(l):
    for i in range(1,len(l)):
        for j in range(len(l)-i):
            if l[j]>l[j+1]:
                s=l[j]
                l[j]=l[j+1]
                l[j+1]=s
    return l

list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
print(bubbleSort(list1))