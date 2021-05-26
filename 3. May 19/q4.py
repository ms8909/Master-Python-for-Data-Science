my_list=[1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]
x=len(my_list)
sum=0
for i in range(0,x-1):
    sum=sum+my_list[i]
print("The average of elements in this array is",sum/x)