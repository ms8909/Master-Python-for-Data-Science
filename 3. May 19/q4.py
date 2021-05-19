# Program to print Average of list

my_list = [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]

length = len(my_list)
sum = 0

for i in my_list:
    sum += i

avg = sum / length

print(f"Our List : {my_list} ")
print(f"Total Elements : {length}")
print(f"Average of our List is : {avg} ")