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
