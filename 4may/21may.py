
def printCollatz(n):

   length=0
     
    # while we do not reach 1
   while n != 1:
         
         print(n, end = ' ')
         length=length+1
 
        # If n is odd
         if n & 1:
            n = 3 * n + 1
 
        # If even
         else:
            n = n // 2
 
    # Print 1 at the end
   print(n)
   return length

n = int( input("Enter your number : "))
x= printCollatz(n)
print (x)

 
