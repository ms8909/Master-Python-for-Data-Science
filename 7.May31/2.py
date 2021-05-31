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


list=[1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
list=Selection_Sort(list)
print(list)