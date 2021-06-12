list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

def merge_sort(list1):
    left=[]
    right=[]
    if len(list1)>1:
        m=int (len(list1)/2)
        for i in range(m):
            left.append(list1[i])
        for i in range(m,len(list1)):
            right.append(list1[i]) 
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list1[k] = left[i]
                i += 1
            else:
                list1[k] = right[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(left):
            list1[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            list1[k] = right[j]
            j += 1
            k += 1
    return(list1)                     

print(merge_sort(list1))