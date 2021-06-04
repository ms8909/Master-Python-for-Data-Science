def Selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if(arr[i]>arr[j]):
                p=arr[i]
                arr[i]=arr[j]
                arr[j]=p
                print(arr)
    return arr
list=[1,5,67,3,8,89,100,4,8,33,55,24]
list=Selection_sort(list)
print("sorted=>", list)