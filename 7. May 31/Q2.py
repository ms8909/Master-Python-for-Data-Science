def selectionSort( itemsList ):
    n = len( itemsList )
    for i in range( n - 1 ): 
        min_Value_Index = i

        for j in range( i + 1, n ):
            if itemsList[j] < itemsList[min_Value_Index] :
                min_Value_Index = j

        if min_Value_Index != i :
            temperory = itemsList[i]
            itemsList[i] = itemsList[min_Value_Index]
            itemsList[min_Value_Index] = temperory

    return itemsList


list1 = [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4]

print("Here is the sorted list: ",selectionSort(list1))
