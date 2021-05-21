print("Please Enter a number : ",end="")
num = int(input())
counter=1
print("The collatz chain is: ",num,end="")
while num!= 1:
    if num%2==0:
        num=int(num/2)
    else:
        num=num*3+1    
    print(" - ",num,end="")
    counter+=1
print("\nThe length of collatz chain is ",counter)        