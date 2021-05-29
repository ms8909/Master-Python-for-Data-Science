# ARHAM RUMI

# Program to Linear Search

# Problem Statement

# --------------------------------------------------------------------------------------
# Let’s suppose we have a list
# list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

# Write a function that takes in two inputs
# A “number”
# “list1”

# The function finds the index of the “number” in “list1”.
# The function should return the index number
# --------------------------------------------------------------------------------------

print("Perform Linear Search on a List")
print("\r")


def linearSearch(num, list1):

    length = len(list1)
    for i in range(0, length):
        if list1[i] == num:
            index = i
            return index
    return -1


def linearSearchAllIndex(num, list1):

    IndexList = []
    length = len(list1)
    for i in range(0, length):
        if list1[i] == num:
            IndexList.append(i)
    return IndexList


list1 = [1, 5, 67, 2, 43, 6, 4, 2, 2, 4, 6, 2, 1, 68, 5, 4]
print("\r")
print(f"Our List is : {list1}")
print("\r")

num = int(input("Enter a Number from above List to get it's INDEX : "))

numIndex = linearSearch(num, list1)
print("\r")

if numIndex == -1:
    print(f" {num} Does NOT exist in the List")
else:
    print(f"Index of {num} is {numIndex} at it's FIRST OCCURRENCE")
    print("\r")
    print(f"All the Indexes of {num} are :  {linearSearchAllIndex(num, list1)}")
