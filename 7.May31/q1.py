
list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]


def BubbleSort(list1):
    # Calculating length
    n = len(list1)
    # Outer loop going from (0 to n-1) with each loop sorting i elements from right
    for i in range(n-1):
        # inner loop
        for j in range(0,n-i-1):
            # Swapping Condition
            if list1[j] > list1[j+1]:
                # Swapping
                list1[j], list1[j+1] = list1[j+1], list1[j]



BubbleSort(list1)

print(list1)
