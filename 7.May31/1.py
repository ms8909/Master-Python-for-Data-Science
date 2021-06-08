# Bubble Sort

def Bubble_Sort(arr):
    a=len(arr)
    for x in range(1,a): 
        for j in range (a-x):
            if(arr[j]>arr[j+1]):
                p=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=p
    return arr
 


list=[1,5,79,43,6]
list=Bubble_Sort(list)
print("Sorted => ",list)