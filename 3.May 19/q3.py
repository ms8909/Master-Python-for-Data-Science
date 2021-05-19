sum=0
product=1
count=0
while True:
    print("Enter integer or press q to quit")
    y=input()
    if y=="q":
        break
    x=int(y)
    count=count+1
    sum=sum+x
    product=product*x
print("The average of integers is",sum/count)
print("The product of integers is",product)   