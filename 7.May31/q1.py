def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):

        for j in range(0, n-i-1):
            
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr           
list1 = [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4]
  
list2=bubbleSort(list1)
print ("Sorted array is:")
print(list2)
