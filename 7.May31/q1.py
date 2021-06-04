def Bubble_Sort():
    list1 = []
    length = int(input("Enter length of list: "))
    for a in range(length):
        print("Enter input on [",a,"] index: ",end="")
        user = int(input())
        list1.append(user)

    for i in range (length):
        flag = 0
        for j in range(length-1-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
                flag=1
        if flag==0:
            break
    return list1
print(Bubble_Sort())