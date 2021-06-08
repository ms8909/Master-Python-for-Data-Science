# ARHAM RUMI

# Program to perform Insertion sort

# Problem Statement

# --------------------------------------------------------------------------------------
# Let’s suppose we have a list
# list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

# Write a function that
# takes list1 an input
# Sort all elements in the list in an ascending order
# Returns the sorted list

# Note: You are not allowed to use the list build-in function .sort()
# --------------------------------------------------------------------------------------

print("We will sort your List")


def insertionSort(list1):

    length = len(list1)

    for i in range(1, length):

        test_element = list1[i]

        # For comparison with other indexes
        j = i - 1
        while j >= 0 and test_element < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = test_element
    return list1


print("\r")

list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

print(f"Unsorted List : {list1}")
print("\r")

sortedlist = insertionSort(list1)

print(f"Sorted List   : {sortedlist}")