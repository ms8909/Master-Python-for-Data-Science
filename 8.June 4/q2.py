#Selection sort


list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

def Selectionsort(list1):
    n = len(list1)
    for i in range(n):
        minIndex = i
        for j in range(i+1,n):
            if list1[minIndex] > list1[j]:
                minIndex = j

        list1[i], list1[minIndex] = list1[minIndex], list1[1]

Selectionsort(list1)

print(list1)
            