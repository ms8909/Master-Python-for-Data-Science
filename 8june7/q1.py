# Q1: Insertion Sort

def insertionSort(list):
    for i in range(1,len(list)):
        j=i-1 
        while j>=0 :
            if(list[i]<list[j]):                
                p=list[j]
                list[j]=list[i]
                list[i]=p
                i-=1
            j=j-1

    return list


list1= [1,5,67,2,43]
list1=insertionSort(list1)
print(list1)
© 2021 GitHub, Inc.