list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

# Start by the first element
# Move each element to their right position
# Swap other elements to their right

def insertion_sort(list1):
    for i in range (1,len(list1)):
        key=list1[i]
        j=i-1
        while j>=0 and list1[j]>key:
            list1[j+1]=list1[j]
            j=j-1
        list1[j+1]=key 
    return list1   
        
print(insertion_sort(list1))    