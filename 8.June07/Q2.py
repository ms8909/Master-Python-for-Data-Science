# Q2 Done by me and sir mudassar

def mergeSort(list1):
   
    if(len(list1)>1):
        mid=int(len(list1)/2)
        Left=[]
        Right=[]
        for i in range (mid):
            Left.append(list1[i])
        for j in range (mid,len(list1)):
            Right.append(list1[j])
        sortedLeft=mergeSort(Left) 
        sortedRight=mergeSort(Right)
        mergedlist=merge(sortedLeft,sortedRight)
        return mergedlist
    else:
        return list1

def merge(Left,Right):
    list1=[]
    i=0
    j=0
    while i<len(Left) and j<len(Right):
        if(Left[i]<Right[j]): 
            list1.append(Left[i])
            i+=1
        else:
            list1.append(Right[j])
            j+=1
    while i<len(Left):
        list1.append(Left[i])
        i+=1
    while j<len(Right):
        list1.append(Right[j])
        j+=1
    return list1
    

list1=[1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4]
print("Un-Sorted==> ",list1)

list2=mergeSort(list1)
print("Sorted==> ",list2)