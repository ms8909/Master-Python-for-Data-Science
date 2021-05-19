#Print average from user input


Sum=0
Count=0
while True:
    print("Enter the number (enter q to exit)")
    num = input()
    if num=="q" or num=="Q":
        break
    num = int(num)
    Count+=1
    Sum+=num

print("The average of numbers entered is ", Sum/Count)