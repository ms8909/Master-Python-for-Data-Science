def ascii_sum(s,l):
    str1=s
    l1=l
    sum=0
    for i in range(l1):
        sum=sum+(ord(str1[i]))
    print("Total ASCII sum:  ",sum)

def ascii_sum_odd(s,l):
    str1=s
    l1=l
    o_sum=0
    for i in range(l1):
        os=ord(str1[i])
        if os%2==1:
            o_sum=o_sum+os
    print("ASCII Sum of odd-numbered charaters:  ",o_sum)

def ascii_sum_even(s,l):
    str1=s
    l1=l
    e_sum=0
    for i in range(l1):
        es=ord(str1[i])
        if es%2==0:
            e_sum=e_sum+es
    print("ASCII Sum of even-numbered charaters:  ",e_sum)

x=input("Enter a string:  ")
y=len(x)
ascii_sum(x,y)
ascii_sum_odd(x,y)
ascii_sum_even(x,y)



    