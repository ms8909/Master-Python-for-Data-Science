print("Enter Value")
num=int(input())
my_list=[]

while num>1:
    if num%2==0:
        num=num/2
        print(num,end="-")
    else:
         num=(num*3)+1
         my_list.append(str(1))
         print("chain = ", (my_list) )
         print("Length = ", len(my_list))
