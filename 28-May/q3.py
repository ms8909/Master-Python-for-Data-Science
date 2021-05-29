print("[1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]")
print("Enter Number to find index")
num=int(input())
list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
def search(num,list):
    index=[]
    for i in range(len(list1)):
        if num==list[i]:
            index.append(i)
    return index
print("Index ", num ,"=",search(num,list1))





