

# # Let’s sort the array using Selection sort

# def Selection_Sort(arr):

#     s=len(arr)

#     for x in range(s):

#         for i in range(x,s):

#             if(arr[x]>arr[i]):
#                 p=arr[x]
#                 arr[x]=arr[i]
#                 arr[i]=p
#     return arr


# listone=[1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

# listone=Selection_Sort(listone)

# print(listone) 



 #Let’s sort the array using Bubble sort
def Bubble_Sort(arr):

    s=len(arr)
    for x in range(s):
        for j in range (1,s):
            if(arr[j]>arr[j+1]):
                p=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=p
    return arr

listone=[1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

list=Bubble_Sort(listone)

print(listone) 
