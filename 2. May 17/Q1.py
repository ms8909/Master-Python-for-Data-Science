#THIS CODE CODED BY NAVEED TARIQ -> GITHUB: @naveid19


print("Please enter any two numbers")
N1 = int(input())
N2 = int(input())
print("Now enter One operator ( +, -, *, /, or %) to perform calculations")
operator =  input()

if operator == "+": 
    print("Your answer is :")
    print(N1+N2)

elif operator == "-": 
    print("Your answer is :")
    print(N1-N2)

elif operator == "*": 
    print("Your answer is :")
    print(N1*N2)

elif operator == "/": 
    print("Your answer is :")
    print(N1/N2)

elif operator == "%": 
    print("Your answer is :")
    print(N1%N2)

else : 
    print("Invalid operator")