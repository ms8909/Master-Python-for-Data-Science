# [Strings] DNA Reverse Complement


# To Reverse Given DNA
def reverse(a):
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    for x in range(len(a)):
        if(a[x]=="A"):
            sum1+=1
        elif(a[x]=="C"):
            sum2+=1
        elif(a[x]=="G"):
            sum3+=1
        elif(a[x]=="T"):
            sum4+=1
    b=["A"*sum4,"C"*sum3,"G"*sum2,"T"*sum1]
    return b

# To Give Reversed Compliment Form Of DNA String 
def complement(a):
    b=reverse(a)
    print("Reversed DNA:",end=" ")
    for x in range(len(b)):
        print(b[x],end="",sep="")

# To Check If The Given String Is Valid DNA Or Not
def check(a):    
    if(len(a)==10):
        return True
    else:
        return False

#Main Function:
print()
a=input("Enter A DNA String: ")

# print(reverse(a))

if(check(a)==True):
    print()
    complement(a)

else:
    print("Invalid String!!!")