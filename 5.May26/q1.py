def ascii_sum(s):
    sum=0
    for i in s:
        sum += ord(i)

    return sum

def ascii_sum_odd(s):
    sum=0
    for i in s:
        val=ord(i)
        # print(i," ",val," ") / for testing only
        if val%2 !=0:
            sum += val
            # print(i," ",val," ",sum) / for testing only

    return sum

def ascii_sum_even(s):
    sum=0
    for i in s:
        val=ord(i)
        # print(i," ",val," ") / for testing only
        if val%2 ==0:
            sum += val
            # print(i," ",val," ",sum) / for testing only
    
    return sum

s = input("Enter a string : ")
print("Total ASCII Sum : ",ascii_sum(s))
print("ASCII Sum of Odd-numbered characters : ",ascii_sum_odd(s))
print("ASCII Sum of Even-numbered characters : ",ascii_sum_even(s))
