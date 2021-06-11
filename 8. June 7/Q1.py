# Insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
 
        current_value = arr[i]

        j = i-1
        while j >= 0 and current_value < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = current_value
 

list1 = [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
sorted_array = []
insertionSort(list1)
for i in range(len(list1)):
    sorted_array.append(list1[i])

print(sorted_array)