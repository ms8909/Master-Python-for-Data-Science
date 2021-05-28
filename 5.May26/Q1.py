def ascii_sum(s):
    sum=0
    for x in range(len(s)):
        sum=sum+ord(s[x])
    return sum

#For Odd-ASCII Characters
def ascii_sum_odd(s):
    sum=0
    for x in range(len(s)):
        if((x+1)%2==1):
            sum=sum+ord(s[x])
    return sum

#For Even-ASCII Characters
def ascii_sum_even(s):
    sum=0
    for x in range(len(s)):
        if((x+1)%2==0):
            sum=sum+ord(s[x])
    return sum

#Main Function
a=input("Enter A String: ")
print("Total ASCII Sum: ",ascii_sum(a))
print("ASCII Sum Of Odd Numbered Characters: ",ascii_sum_odd(a))
print("ASCII Sum Of Even Numbered Characters: ",ascii_sum_even(a))