List1 = [1,3,4,2]
for i in range(1,len(List1)):
  current_index=0
  for i in range(len(List1)-i):
        x1=List1[current_index]
        x2=List1[current_index+1]
        if x1>x2:
             List1[current_index]=x2
             List1[current_index+1]=x1
       

        current_index=current_index+1
print(List1)