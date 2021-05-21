def collatz_sequence(x):
    num_seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
       num_seq.append(x)    
    return num_seq

y=int(input("Enter a number: "))
print(collatz_sequence(y))
print("The length of collatz chain is:", len(num_seq))


