num=0
avg=0
product=1
x=0
print("To End Entries Enter 'end'")
while num !="end":
    num=input("Enter Number: ")
    if(num!="end"):
        num=int(num)
        x=x+1
        avg=avg+num
        product=product*num
print("Average: ",avg/x)
print("Product: ",product)5
