list = [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4]
def selection_sort():
    for j in range(len(list)):
        a = 0
        for i in range(1,len(list)):
            a1 = list[a]
            a2 = list[i]
            if list[a]>list[i]:
                list[a] = a2
                list[i] = a1
            a = a + 1
    return list
print("Ascending Order of Array by Selection Sort is: ",selection_sort())