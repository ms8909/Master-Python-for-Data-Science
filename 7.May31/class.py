list1= [2,4,6,2,7,8,9,10,23,43,22 ]

for i in range(1,len(list1)):
  current_index=0
  for i in range(len(list1)-i):
        x1=list1[current_index]
        x2=list1[current_index+1]
        if x1>x2:
             list1[current_index]=x2
             list1[current_index+1]=x1
       

        current_index=current_index+1
print(list1)
