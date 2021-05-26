print("Enter a string")
s=input()
y=len(s)   
    
def ascii_sum(string):
    total_sum=0  
    for i in range(y):
        z=ord(s[i])
        total_sum=total_sum+z
    return(total_sum)     

def ascii_sum_even(string):
    even_sum=0  
    for i in range(y):
        z=ord(s[i])
        if z%2==0:
            even_sum=even_sum+z
    return(even_sum) 

def ascii_sum_odd(string):
    odd_sum=0  
    for i in range(y):
        z=ord(s[i])
        if z%2==1:
            odd_sum=odd_sum+z
    return(odd_sum) 

print("Total Ascii sum: ",ascii_sum(s))
print("Ascii sum of odd character is: ",ascii_sum_odd(s))
print("Ascii sum of even character is: ",ascii_sum_even(s))