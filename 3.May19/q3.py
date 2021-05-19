#Average and Product

entry=0
avg=0
product=1
x=0
print("To End Entries Enter 'q'")
while entry !="q":
    entry=input("Enter Number: ")
    if(entry!="q"):
        entry=int(entry)
        x=x+1
        avg=avg+entry
        product=product*entry
print("Average: ",avg/x)
print("Product: ",product)


