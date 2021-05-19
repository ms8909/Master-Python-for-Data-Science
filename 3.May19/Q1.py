a = int(input("Enter Any Number"))
fac = 1
for i in range(1, a + 1):
	fac = fac * i
if a<0:
    print("Enter positive number")
else:
    print("factorial of ", a, " is ", fac)



