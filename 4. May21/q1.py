print("Enter any positive integer")
x=int(input())
my_list=[x]
while x>1:
    if x%2==0:
        x=x/2
    else:
        x=3*x+1
    my_list.append(x) 

print("The collatz chain is:", my_list)
print("The length of collatz chain is:", len(my_list))

