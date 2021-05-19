prod=1
avg=0
i=1

while i :
    ch = input()
    if(ch == 'q'):
        break
    else:
        num = int(ch)
        prod*=num
        avg+=num
        i+=1

print("The product is "+str(prod)+" and the average is "+str(avg/(i-1)))        
