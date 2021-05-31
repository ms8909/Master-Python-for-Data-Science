list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

def bubbleSort(list1):
    n = len(list1)
  
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if list1[j] > list1[j+1] :
                list1[j], list1[j+1] = list1[j+1], list1[j]
  

  
bubbleSort(list1)
  
print ("Sorted array is:")
for i in range(len(list1)):
    print ("%d" %list1[i]), 