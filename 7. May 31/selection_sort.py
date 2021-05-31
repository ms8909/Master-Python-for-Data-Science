# ARHAM RUMI

# Program to perform Selection sort

# Problem Statement

# --------------------------------------------------------------------------------------
# Let’s suppose we have a list
# list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

# Write a function that
# takes list1 an input
# Sort all elements in the list in a asscending order
# Returns the sorted list

# Note: You are not allowed to use the list build-in function .sort()
# --------------------------------------------------------------------------------------

print("We will sort your List")


def selectionSort(list1):
    length = len(list1)
    for i in range(length-1):
        minimum_index = i
        for j in range(i+1, length):
            if list1[j] < list1[minimum_index]:
                minimum_index = j
        list1[i], list1[minimum_index] = list1[minimum_index], list1[i]
        

    return list1


print("\r")

list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

print(f"Unsorted List : {list1}")
print("\r")

sortedlist = selectionSort(list1)

print(f"Sorted List   : {sortedlist}")