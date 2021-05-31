def acsii(s):
    sum=0

    for item in range(0, len(s)):
        unicode=ord(s[item])
        
        sum=sum+unicode
        print("The sum of ASCII is " , sum)


print("Enter a character")
s=input()

acsii(s)

# EVEN FUNCTION

def acsii_even(s):
    sum=0

    for item in range(0, len(s)):
        unicode=ord(s[item])
        if unicode%2==0:
            sum=sum+unicode
        print("The sum of even ASCII " , sum)


#print("Enter a character")
#s=input()

acsii_even(s)

# ODD FUNCTION

def acsii_odd(s):
    sum=0

    for item in range(0, len(s)):
        unicode=ord(s[item])
        if unicode%2!=0:
            sum=sum+unicode
        print("The sum of even ASCII " , sum)


#print("Enter a character")
#s=input()

acsii_odd(s)






