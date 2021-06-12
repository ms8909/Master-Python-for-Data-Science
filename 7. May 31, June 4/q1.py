list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4]

def bubble_sort (list1):
    for j in range(1,len(list1)) :
        for i in range (len(list1)-j):
            x1=list1[i]
            x2=list1[i+1]
            if x1>x2:
                list1[i]=x2
                list1[i+1]=x1       
    return list1                
               
print(bubble_sort(list1))     
          
        
