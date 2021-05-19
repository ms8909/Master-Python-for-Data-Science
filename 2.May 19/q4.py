my_list= [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]
int_sum = 0 
count = 0

for i in my_list:
  int_sum += i
  count += 1

print('Average = ', int_sum/count)  