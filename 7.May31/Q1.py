list = [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4]
def bubble_sort():
    for i in range(1,len(list)):
        index = 0
        for i in range(1,len(list)):   
            a1 = list[index]
            a2 = list[index + 1]
            if a1>a2:
                list[index] = a2
                list[index + 1] = a1
            index = index +1
    return list
print("Ascending Order of Array by Bubble Sort is: ",bubble_sort())