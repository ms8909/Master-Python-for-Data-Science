def selectionSort(l):
    
    for i in range(len(l)):
        minindex=i
        sel=l[i]
        # print("Sel = ",sel," and i = ",i," and l[",i,"] = ",l[i])
        for j in range(i+1,len(l)):
            # print("Sel = ",sel," and i= ",i," and j = ",j," and l[",j,"] = ",l[j])
            if sel>l[j]:   
                # print("Condition is true and current minindex = ",minindex,"and sel is ",sel," and l[j] is ",l[j]," at j=",j)
                minindex=j 
                sel=l[j]
                # print("Updated minindex = ",minindex,"and sel is ",sel," and l[j] is ",l[j]," at j=",j)    
        if i != minindex:
            # print("while swapping minindex = ",minindex,"and i is ",i," and l[i] is ",l[i]," and l[minindex]=",l[minindex])
            s=l[i]
            l[i]=l[minindex]
            l[minindex]=s
            # print("Updated Array ",l)
    return l

list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
print(selectionSort(list1))