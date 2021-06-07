def insertionSort(arr):
     
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr;
 
 
# Driver code to test above
list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
a=insertionSort(list1)
print("Sorted array is : ")
print(a)