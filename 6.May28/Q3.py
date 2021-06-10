list = []
print("Enter Array Elements: ")
def ind():
    for i in range(16):
        a = int(input())
        list.append(a)
    print(list)
    n = int(input("Enter Number to find Index Number or it: "))
    return list.index(n)
print("Index Number of is: ",ind())