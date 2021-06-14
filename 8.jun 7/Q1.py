def insertion_sort(list):
    lst=list
    for i in range(1, len(lst)):
        for j in range(i - 1, -1, -1):
            if(lst[j] > lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
print(insertion_sort(list1))