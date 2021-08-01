list1 = [1, 5, 67, 2, 43, 6, 4, 2, 2, 4, 6, 2, 1, 68, 5, 4]

newlist = []

while list1:
    minimum = list1[0]
    for x in list1:
        if x < minimum:
            minimum = x
    newlist.append(minimum)
    list1.remove(minimum)

print(newlist)
