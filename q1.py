list1= [1,5,67,2,43]
arr=len(list1)
for i in range (1,arr):
    for j in range (arr-i):
        if list1[j]>list1[j+1]:
            p = list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=p

print("list=>", list1)