# is_prime function
def is_prime(n):

    n_stirng=str(n)
    sum= 0
    for i in n_stirng: # for the sum of a number's digits
        convert_to_int = int (i)
        tsum = sum + convert_to_int
        sum = convert_to_int

    #                        *********** CONDITIONS ***********
    #If the sum of a number's digits is a multiple of 3, that number can be divided by 3.
    #The only even prime number is 2. All other even numbers can be divided by 2.
    #No prime number greater than 5 ends in a 5. Any number greater than 5 that ends in a 5 can be divided by 5.

    # To fulfil above 3 conditions
    if (n%2 == 0 and n!=2 )  or (tsum%3 == 0 and tsum==3 and n!=3) or (n%5 ==0 and n!=5) or n ==1 or n==0:
        return(False) # False for not prime
    else:
        return(True) # True for prime

# factors function
def factors(n) :

    factors_list = [] #Empty list to store factors number
    for i  in range(1,n+1):
        
        if n%i==0 :
            factors_list.append(i)

    return(factors_list)

# prime_factors function
def prime_factors(n):

    n_list =  n
    prime_factors_list = [] # Take an empty list to store prime numbers from factors list

    for i in range(len(n_list)):
        check_prime = n_list[i]
        prime_input =  check_prime
        if is_prime(prime_input) == True: #calling of is_prime function
            prime_factors_list.append( prime_input)

    return(prime_factors_list)


#Taking input from user
in_put = input("Enter the value: ")

p_factors_input =  int(in_put) #Converting into int data type
f = factors(p_factors_input) # calling function and storing in 'f'
p=prime_factors(f) # calling function and storing in 'p'

#Printing of the lists
print("List of Factors of the given input: ",f)
print("List of Prime numbers from the list of Factors: ",p)