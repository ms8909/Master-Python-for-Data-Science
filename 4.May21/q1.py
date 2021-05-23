count = 1 

def collatz(number):

    if number % 2 == 0:
        number = number // 2
        print(number)
        return number

    elif number % 2 != 0:
        number = number * 3 + 1
        print(number)    
        return number

number = int(input("Please Enter a Positive Number: "))
while number > 1:
    count +=1
    number = collatz(number)

print("this is count: ", count)

