# Program to apply Collatz Conjecture

# If the number is odd, multiply it by 3 and add 1  (3n+1) 
# If the number is even, divide it by 2 (n/2)

def collatzConjecture(num):
    collatzChain = [num]
    
    if num < 1 or num == 0:
        print("Please Enter a Positive Integer")
    else:
        if num == 1:
            print("Number is already 1 and the chain length is 1")
        else:
            while num != 1:
                if num % 2 == 0:
                    num = num // 2
                    collatzChain.append(num)
                else:
                    num = (3 * num) + 1
                    collatzChain.append(num)
            
            chainLen = len(collatzChain)
            collatzChain.reverse()

            print(f"Collatz Chain : ", end="")

            for i in range(chainLen):
                print(f"{collatzChain.pop()} - ", end="")

            print("\r")
            print(f"Chain Length is : {chainLen} ")

# Main code
num = int(input("Enter a positive integer to apply the collatz Conjecture : "))
collatzConjecture(num)