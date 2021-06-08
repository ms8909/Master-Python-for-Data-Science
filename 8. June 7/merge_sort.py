# ARHAM RUMI

# Program to perform Merge sort

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


def mergeSort(list1):

    length_list1 = len(list1)   # Length of Main List

    if length_list1 > 1:

        # Dividing in two halves
        mid = length_list1 // 2
        left = list1[:mid]  # Left Half
        right = list1[mid:] # right Half

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        left_current = 0       # Iterator for left half
        right_current = 0      # Iterator for right half
        main_list_current = 0  # Iterator for the main list

        length_left_half = len(left)    # Length of Left Half
        length_right_half = len(right)  # Length of right Half

        while left_current < length_left_half and right_current < length_right_half:

            # Comparing Left Current Element with Right Current Element and inserting it into the main list if the Left Current Element is LESS than or EQUAL to the Right Current Element
            if left[left_current] <= right[right_current]:
              list1[main_list_current] = left[left_current]
              left_current += 1    # Move the iterator one index forward

            # Insert Right Current Element into the main list if the Left Current Element is GREATER than the Right Current Element
            else:
                list1[main_list_current] = right[right_current]
                right_current += 1  # Move the iterator one index forward
            main_list_current += 1  # Move the iterator one index forward
            
        # Merging the Left Half into the maian list
        while left_current < length_left_half:
            list1[main_list_current] = left[left_current]
            left_current += 1
            main_list_current += 1

        # Merging the Right Half into the maian list
        while right_current < length_right_half:
            list1[main_list_current]=right[right_current]
            right_current += 1
            main_list_current += 1        

    return list1


print("\r")

list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

print(f"Unsorted List : {list1}")
print("\r")

sortedlist = mergeSort(list1)

print(f"Sorted List   : {sortedlist}")