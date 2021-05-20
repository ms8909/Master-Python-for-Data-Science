i=0
a=100
n=0
product=1;
while i <= a:
    print('Enter the input')
    user_input=str(input())
    if user_input!='q':
        n=n+int(user_input)
        product = n*product
        print('Enter to continue or q to quit')
        i=i+1
        
    else:
        print('You have chosen to quit')
        break
avg=n/i
print("total time the user entered the value is : %d " %i)
print("Average : %d" %avg)
print("product of all the given numbers : %d" %product)