def ascii_sum(s,l):
    str1=s
l1=l
sum=0
for i in range(l1):
    sum=sum+(ord(str1[i]))
    print("Total Ascii sum:", sum)

def ascii_odd(s,l):
    str1=s
    l1=l
    o_sum=0
    for i  in range (11):
        os=ord(str1[i])
        if os%2==1:
            o_sum=o_sum+os   
        print("Sum odf Odd ",o_sum)

def ascii_sum_even(s,l):
    str1=s
    l1=l
    e_sum=0
    for i in range(l1):
        es=ord(str[i])
        if es%2==0:
            e_sum=e_sum+es
            print("Sum of even Ascii is:", e_sum)
            x=input("Enter String")
            y=len(x)
            ascii_sum(x,y)
            ascii_odd(x,y)
            ascii_sum_even(x,y)




