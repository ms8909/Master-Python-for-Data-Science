#Pattern using for loop


#Part a


for i in range(4):
    str = "*"*(i+1)
    print(str)


#Part b

j=1
space = 2
addCheck = True
for i in range(5):
    str = " "*space + "*"*(j)
    if j<5 and addCheck==True:
        j+=2
        space-=1
    else:
        addCheck = False
        j-=2
        space+=1
    print(str)



#part c

def invert(num):
    if num ==1:
            return 0
    else:
        return 1


num = 1
linerange = 7
for i in range(4):
    print(" "*i, end="") #Printing spaces needed at the start
    for j in range(linerange):
        print(num,end="")
        num = invert(num)
    num = invert(num) #Inverting back to 1 at the end of the inner loop
    linerange -=2 #Changing the total numbers needed to be printed
    print() # For next line
