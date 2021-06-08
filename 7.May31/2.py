# Selection Sort

def Selection_Sort(arr):
    a=len(arr)
    for x in range(a):
        for i in range(x,a):
            if(arr[x]>arr[i]):
                p=arr[x]
                arr[x]=arr[i]
                arr[i]=p
    return arr


list=[1,5,67,2,1]
list=Selection_Sort(list)
print("Sorted => ",list)