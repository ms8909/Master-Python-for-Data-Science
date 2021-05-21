a= int(input("Enter Number"))
def collatz_sequence(a):
    num_seq = [a]
    if a < 1:
       return []
    while a > 1:
       if a % 2 == 0:
         a = a / 2
       else:
         a = 3 * a + 1

       num_seq.append(a)    
    return num_seq

print(collatz_sequence(a))


