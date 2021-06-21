n = 0
t = 0
a = 10
while n <= a:
    num = str(input("Enter Input: "))

    if num!= 'q':
        t-t+int(num)
        print("press q to quit")
        n = n+1
    else:
        print("Input Quit")
        break

    average= t/n
    print("Average: ", average)
    print("product: ", t)