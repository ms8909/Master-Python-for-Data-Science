#ASCII Sums


#Part 1
def ascii_sum(s):
    sum = 0
    for c in s:
        sum += ord(c)
    return sum;


st = 'Mateen'

print(len(st))

print("Sum of ascii values for", st, "is", ascii_sum(st))

#Part 2

def ascii_sum_odd(s):
    sum=0
    for i in range(len(s)):
        if i%2==0:
            sum+=s[i]
    return sum


#Part 3

def ascii_sum_even(s):
    sum=0
    for i in range(len(s)):
        if i%2!=0:
            sum+=s[i]
    return sum
