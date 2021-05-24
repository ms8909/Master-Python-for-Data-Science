num=int(input("inter your number"))
while num>1:
    if num%2==0:
        num=num/2
        print(num)

    elif num%2==1:
         num=(num*3)+1
         print(num)
