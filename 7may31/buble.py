
def bubble_sort(arr):

    s=len(arr)
    for x in range(1,s):
        for j in range (s-x):
      
            if(arr[j]>arr[j+1]):
             p=arr[j]
             arr[j]=arr[j+1]
             arr[j+1]=p
        return arr
list=[7,5,67,4,3]
list=bubble_sort(list)
print(list)


