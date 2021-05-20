
#                Taking an input to check the factorial..................
a = int(input("Enter the number to check the factorial"))
factorial = 1

# check if the number is negative, positive or zero
if a < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif a == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, a + 1):
        factorial = factorial*i
    print("The factorial of", a, "is....", factorial)
