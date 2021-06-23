# insertionsort

list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

def insertion_sort(array):

    for i in range(1, len(array)):
        key_item = array[i]

        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array