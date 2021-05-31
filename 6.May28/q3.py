def search(l,n):
    index=-1
    for i in range(len(l)):
        if n==l[i]:
            index=i
            break
    return index

list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
num=68
index=search(list1,num)
if index == -1:
    print("The value was not found")
else:
    print("The index of ",num," in list is ",index)