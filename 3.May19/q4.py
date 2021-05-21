#Calculating average of list of numbers


my_list= [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]

sum = 0
length = len(my_list)
for i in range(length):
    sum+=my_list[i]

average = sum/length


print("Sum of numbers was ", sum)
print("Their average was ", average)