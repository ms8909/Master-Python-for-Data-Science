#Dictinaries and arrays



print("Please enter the number of inputs")

N = int(input())

arr = [{}]*N
for i in range(N):
    print("Name:", end="")
    name = input()
    print("Age:", end="")
    age = input()
    print("Phone Number:", end="")
    PH = input()
    print("Address:", end="")
    add = input()
    dic = {"name": name, "Age": int(age), "PhoneNumber": int(PH), "Address": add}
    arr[i]=  dic

print(arr)
