def Collatz_Chain(col_num): #created function
    counting= 1
    print("The collatz chain is: ", end="")
    while col_num != 1: 
        print(col_num, end="-")
        if col_num%2 == 0:
            col_num= col_num /2
            col_num = int (col_num)
                    
        elif col_num%2 != 0: #converting odd to even
            col_num= ((3*col_num)+1)
            col_num= int(col_num)
        
        counting=counting+1   
    
    print(col_num)     
    print ("Collatz chain length: ",counting)

col= int (input("Please enter a number : ")) #taking input
print()
Collatz_Chain(col) #calling function
print()