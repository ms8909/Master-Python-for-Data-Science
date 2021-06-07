#Selection Sort


list1= [1,5,67,2,43,6,4,2,-1,4,6,2,1,68,5,41]








def SelectionSort(list1):
    n = len(list1) #Length of array
    for i in range(n):

        #Finding Minimum index
        minIndex = i
        for j in range(i+1,n):
            if list1[minIndex] > list1[j]:
                minIndex = j

       #list1[minIndex]  = minimum number in the array
        
        list1[i], list1[minIndex] = list1[minIndex], list1[i]

        


SelectionSort(list1)

print(list1)