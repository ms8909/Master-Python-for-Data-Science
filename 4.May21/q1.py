def collatz_sq(x):
    count=1
    num_seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
       count=count+1  
    # Added line
       num_seq.append(x)  
    print("Count is : ")
    print(count)   
    return num_seq

n=int(input("Enter a number : "))
ans=collatz_sq(n)
print("The collatz chain is:")
print(ans)
  
    
       
