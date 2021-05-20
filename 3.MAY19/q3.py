#question no 3
print("enter num")
mul=1
sum=0
a=0
while 1:
    num=int(input())
    a=a+1
    sum=sum+num
    mul=mul*num
    print("Press q to quite code or press y to continue")
    m=input()
    if m=='q':
        break
    
    
print("Average",sum/a)
print("product",mul)
