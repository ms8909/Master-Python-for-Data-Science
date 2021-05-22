num = int(input("Enter yout number"))
fact = 1
if num < 0:
    print("no factorial")
else:
    for i in range(1, num + 1):
        fact = fact *i
        print("The fact of ", num, "is", fact)