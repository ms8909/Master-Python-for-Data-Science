num=5
for i in range(1,(num+1)//2+1):
    for j in range((num+1)//2-i):
        print(" ",end="")
    for k in range((i*2)-1):
        print("*",end="")
    print("")

for i in range((num+1)//2+1,num+1):
    for j in range(i-(num+1)//2):
        print(" ",end="")
    for k in range((num+1-i)*2-1):
        print("*",end="")  
    print("")      
