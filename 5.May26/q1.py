
# ascii_sum(s) function

def ascii_sum(s):

    
    sum=0;

    for item in range(0,len[s]):
    
        unicode=ord(s[item])

        # print(unicode)
        sum=sum+unicode
    print("The sum of all ascii is",sum)
    

print("Enter a character")
s=input()

# function calling
ascii_sum(s)

 
 #even adding function

def ascii_even(s):

    sum=0

    for item in range(0,len(s)):
        unicode= ord(s[item])
        # print(unicode)
        if unicode%2==0:
            sum=sum+unicode
        # else:
        #     print("odd character wil not add in our sum")
    print("The sum of even ASCII are",sum)
  

# print("Enter a characters")
# s=input()

ascii_even(s)

# odd function
        
def ascii_odd(s):
    sum=0
    for item in range(0,len(s)):
        unicode=ord(s[item])    
        # print(unicode)
        if unicode%2!=0:
            sum=sum+unicode
    print("The sum of odd ASCII is",sum)

  
# print("Enter the input")
# s=input()

#function calling
ascii_odd(s)
