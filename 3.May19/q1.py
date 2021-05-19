print("Please input a num")
num = int(input())
number=num
fact=1
if num==1 or num==0:
    fact=1
else:
    while num>1:
        fact = fact * num
        num-=1
print("The factorial of "+str(number)+" is "+str(fact)+".")        
