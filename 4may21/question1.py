counter =1 
def collatzchain(num):
    if num%2==0:
        num=num//2
        print(num)
        return num
    elif num%2!=0:
        num=num*3+1
        print(num)
        return num
num=int(input("enter number "))
while num > 1:
    counter=counter+1
    num=collatzchain(num)
print("this is count",counter)