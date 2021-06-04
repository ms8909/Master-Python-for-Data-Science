def Selection_Sort():
    list1 = []
    length = int(input("Enter length of list: "))
    for a in range(length):
        print("Enter input on [",a,"] index: ",end="")
        user = int(input())
        list1.append(user) 
    for i in range (length):
        for j in range(i,length):
            if list1[i]>list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
    return list1
print(Selection_Sort())