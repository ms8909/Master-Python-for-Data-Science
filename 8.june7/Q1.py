list = [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4]
def insertion_sort():
    for i in range(1,len(list)):
        a = list[i]
        b = i - 1
        for j in range(b):
            if list[b] > a:
                list[b+1] = list[b]
                list[b]  = a
                b = b - 1
    return list
print("Ascending Order of Array by Insertion Sort is: ",insertion_sort())