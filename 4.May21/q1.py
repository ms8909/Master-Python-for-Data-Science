#If n is even, then n = n / 2.
#If n is odd, then n = 3*n + 1.
#Repeat above steps, until it becomes 1.

#Python program to print collatz sequence

n = int(input("Plese enter a number = "))
chain_length = [n]
while n!=1:
    if n%2==0:
        n = n/2
    else:
        n = (3*n)+1
    chain_length.append(n)
print("The collatz chain is:",chain_length)
print("Collatz chain length:",len(chain_length))
