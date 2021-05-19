num = int(input("Enter Your Number: "))

fact = 1
if num < 0:
    print("no factorial")

else:
    for i in range(1, num + 1):
        fact = fact *i
print("The Fact of", num, "is", fact)