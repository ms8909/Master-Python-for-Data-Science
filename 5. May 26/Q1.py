def ascii_sum(s): # total number sum function
    plus = 0
    for i in s:
         
        o=ord (i)
        plus = plus +o

    return(plus)   
    
def ascii_sum_even(s): # only even number sum function
    even = 0
    for i in s:

        o=ord (i)
        int (o)

        if o%2 == 0 :        
            even = even + o
            
    return(even) 

def ascii_sum_odd(s):  # only odd number sum function
    odd  = 0
    for i in s:
         
        o=ord (i)
        int (o)

        if o%2 != 0 :        
            odd = odd + o

    return(odd)

#Taking input from user

st = input("Enter the string : ")

#calling of function
ascii_sum(st)
ascii_sum_even(st)
ascii_sum_odd(st)

#printing of sums
print("Sum of all input strings : ",ascii_sum(st))
print("Sum of all even strings : ",ascii_sum_even(st))
print("Sum of all odd strings : ",ascii_sum_odd(st))