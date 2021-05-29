list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4]
x=2

def linear_search(x,list1):
    index_no=[]
    for i in range(len(list1)):
        if x==list1[i]:
            index_no.append(i)
    return index_no

print("The index number of",x, "in the list is", linear_search(x, list1))
