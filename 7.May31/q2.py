import sys
list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
  
# Traverse through all array elements
for i in range(len(list1)):
      
    # Find the minimum element in remaining 
    # unsorted array
    min_idx = i
    for j in range(i+1, len(list1)):
        if list1[min_idx] > list1[j]:
            min_idx = j
              
    # Swap the found minimum element with 
    # the first element        
    list1[i], list1[min_idx] = list1[min_idx], list1[i]
  
# Driver code to test above
print ("Sorted array")
for i in range(len(list1)):
    print("%d" %list1[i]), 