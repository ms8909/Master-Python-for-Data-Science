n = 0
total=0
a=10
while n <= a:

    num = str(input("Enter Input : "))
    if num!='q':
        total=total+int(num)
        print("Press q to quit or continue")
        n = n+1
    else:
        print("Input Quit.")
        break

average= total/n

print("Average: ", average)
print("Product: ", total)
