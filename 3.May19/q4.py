my_list= [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]

avg=0
counter=0

for i in my_list:
    counter+=1
    avg+=i

print("The average of my_list is "+str(avg/counter))   