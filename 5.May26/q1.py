def ascii_sum(s):
    sum=0
    for i in range(len(strinput)):
        sum = sum + ord(strinput[i])
    return sum
def ascii_sum_odd(s):
    oddsum=0
    for i in range(len(strinput)):
        if ord(strinput[i])%2!=0:
            oddsum=oddsum+ ord(strinput[i])
    return oddsum
def ascii_sum_even(s):
    evensum=0
    for i in range(len(strinput)):
        if ord(strinput[i])%2==0:
            evensum=evensum + ord(strinput[i])
    return evensum
strinput=input(str("Enter the String : "))
sum1=ascii_sum(strinput) 
print("Total ASCII Sum : ",sum1)
oddsum1=ascii_sum_odd(strinput)
print(" ASCII Sum of even numbers characters : ",oddsum1)
evensum1=ascii_sum_even(strinput)
print(" ASCII Sum of odd numbers characters : ",evensum1)  