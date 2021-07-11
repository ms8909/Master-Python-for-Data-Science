def mergeSort(arr,l,r,side):

    if l<r : 
        m= l+(r-l)//2
        # print(arr," when l = ",l," and r = ",r," and m = ",m," side= ",side)        
        mergeSort(arr, l, m,"left")
        mergeSort(arr, m+1, r,"right")
        print(arr," when l = ",l," and r = ",r," and m = ",m," side= ",side)
list1= [1,5,67,2,43,6,3,10]
mergeSort(list1, 0, len(list1)-1,"whole")


# mergesort(0,15)
    # 

