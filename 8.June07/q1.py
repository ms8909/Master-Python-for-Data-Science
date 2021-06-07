#Insertion Sort




def insertionSort(l1):
    n  = len(l1)
    for i in range(1,n):
        key = l1[i]
        j = i-1
        while j>=0 and l1[j]>key:
            l1[j+1] = l1[j]
            j -=1
        l1[j+1]= key


l1 =  [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]


print("Before Sorting", l1)

insertionSort(l1)

print("After Sorting", l1)