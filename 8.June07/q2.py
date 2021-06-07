#merge Sort



def merge(arr,left,middle,right):
    n1 = middle - left+1
    n2 = right- middle

    L = [1]*n1
    R = [1]*n2

    for i in range(n1):
        L[i] = arr[left+i]
    for i in range(n2):
        R[i] = arr[middle+1+i]

    i=0
    j=0
    k=left

    while i<n1 and j<n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    

    
    while i<n1:
        arr[k] = L[i]
        i+=1
        k+=1

    while j<n2:
        arr[k] = R[j]
        j+=1
        k+=1


def mergeSort(l1,l,r):
    if l<r :
        m = int(l+(r-l)/2)

        mergeSort(l1,l,m)

        mergeSort(l1,m+1,r)

        merge(l1,l,m,r)



# Keep on dividing the array until the size of each array is 1
# Then merge two adjacent arrays such it they are sorted
        #   To do this compare left most value in both values and increase the pointer of the array where smaller value is found
    # In this way at the end, we will have a sorted array 



list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

n = len(list1)

mergeSort(list1,0,n-1)

print(list1)