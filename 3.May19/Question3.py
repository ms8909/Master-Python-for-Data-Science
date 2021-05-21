Sum=0
Counting=0
while True:
    print("Enter the number (enter q to exit)")
    n = input()
    if n=="q":
        break
    n = int(n)
    Counting+=1
    Sum+=n
print("The average of numbers entered is= ", Sum/Counting)