list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4]
print(list1)
x=int(input("Enter a number from this list to find the index of that number: "))
def function(number,list1):
    y=number
    index_no=[]
    for i in range(len(list1)):
        if y==list1[i]:
            index_no.append(i)
    return index_no
print("The index number of",x, "in the list is", function(x, list1))