more = "n"
sum = 0
inp= "q"
count = 0
product = 1
while more == "n":
    count = count +1
    x = float(input("Enter Number"))
    sum = (sum + x)
    product = x*product
    print ("Press q when you are done inputting the numbers or n to continue")
    more = input("")
c = sum/count
print ("You Inputed", count, "Numbers")
print ("The Average of the Numbers is ", c)
print ("The product of the numbers is ", product)
