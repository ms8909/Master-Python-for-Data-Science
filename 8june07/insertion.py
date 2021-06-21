# insertion sort

def insertionSort(arr):
   for i in range(1,len(arr)):

     currentvalue = arr[i]
     position = i

     while position>0 and arr[position-1]>currentvalue:
         arr[position]=arr[position-1]
         position = position-1

         arr[position]=currentvalue

arr = [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
insertionSort(arr)
print(arr)
