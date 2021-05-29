def find_Index(num,list):
    index=[]
    for i in range(len(list)):
       if(list[i]==num):
            index.append(i)
    return index
list1=[1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
print("List: ",list1)
no=int(input("Enter a number to find Index : "))
ans=find_Index(no,list1)
print("Index of the given number is : ",ans)