# bubble sort#
def Bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range (len(arr)-i):
            if(arr[j]>arr[j+1]):
                p = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=p
    return arr
list=[1,5,67,66,9,3,2,43,89,4]
list=Bubble_sort(list)
print("sorted=>", list)