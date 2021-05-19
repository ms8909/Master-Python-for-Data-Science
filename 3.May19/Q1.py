number=int(input("Enetr a number: "))
fictorial=1
if number<0:
    print("sorry please enter a positve number")
elif number==0:
    print("Fictorial of 0 is: 1")
else:
    for i in range(1,number+1):
        fictorial=fictorial*i
    print("fictorial of ",number,"is: ",fictorial)

