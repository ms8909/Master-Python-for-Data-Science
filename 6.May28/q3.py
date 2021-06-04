def search(num, lis):
    index = []
    for i in range(len(lis)):
        if num == lis[i]:
            index.append(i)
    return index

list1 = [1, 5, 67, 2, 43, 6, 4, 2, 2, 4, 6, 2, 1, 68, 5, 4]
print(list1)
number = int(input("Enter any number from above list to find its index number: "))

print("The index of", number, "is", search(number, list1))
