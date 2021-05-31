# ARHAM RUMI

# Program to perform Bubble sort

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


def bubbleSort(list1):

    length = len(list1)

    for i in range(length - 1):
        flag = 0

        for j in range(length - 1):

            if list1[j] > list1[j + 1]:
                tmp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = tmp
                flag = 1

        if flag == 0:
            break

    return list1


print("\r")

list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

print(f"Unsorted List : {list1}")
print("\r")

sortedlist = bubbleSort(list1)

print(f"Sorted List   : {sortedlist}")