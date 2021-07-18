print("Start entering numbers")
pro=1
sum=0
c=0
while 1:
    num=int(input())
    c=c+1
    sum=sum+num
    pro=pro*num
    print("Press q when you are done inputting the numbers or y to continue")
    m=input()
    if m=='q':
        break
    
    
print("Average",sum/c)
print("product",pro)