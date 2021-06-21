def select_Sort(arr):

    s=len(arr)
    for x in range(s):
        for j in range (x,s):
            if(arr[x]>arr[j]):
                p=arr[x]
                arr[x]=arr[j]
                arr[j]=p
    return arr

listone=[1,5,67,2,43 ]

list=select_Sort(listone)

print(listone) 
