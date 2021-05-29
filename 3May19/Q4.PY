def Average(my_list):
    return sum(my_list) / len(my_list)
  
# Driver Code
my_list= [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]

average = Average(my_list)
  
# Printing average of the list
print("Average of the list =", round(average, 2))