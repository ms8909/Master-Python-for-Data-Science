print("Enter value which u want Factorial:")
num=int(input())
factorial=1
if num<0:
    print("Factorial of Negative No dosenot exit")
    else:
        for num in range(1,num + 1):
            factorial=factorial*1
            print("Factorial of ",num,"=", factorial)