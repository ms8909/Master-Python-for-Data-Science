def linear_search(number, list):
  return list.index(number) 

list1= [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]
num = int(input('Please enter the number you would like to be searched: '))  

print(linear_search(num, list1))