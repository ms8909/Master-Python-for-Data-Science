def MergeSort(arr):
     if len(arr) > 1:
        mid = int(len(arr)/2)
        L = arr[:mid]
        R = arr[mid:]
        MergeSort(L)
        MergeSort(R) 
        Merge(arr,L,R)

def Merge(arr,L,R):
    i=j=k=0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1

        k+=1
    while j<len(R):
        arr[k]=R[j]
        j+=1
        k+=1
    while i<len(L):
        arr[k]=L[i]
        i+=1
        k+=1

arr=  [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4]
MergeSort(arr)
print(arr)