list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
number=int(input("inter your number"))
def serach(num,lis):
    for a in range(len(list1)):
        if number==list1[a]:
            print(a)
serach(number,list1)