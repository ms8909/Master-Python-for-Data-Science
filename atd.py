print("Total Number of Classes Held")
x = int(input())

print("Total Classes you can Take ")
y = int(input())
z=y*100/x
print("Percantage = " )  
print(z)


if z>=75:
    print("Allow to take exams")
    elif z<75:
        print("donot allow to take exams")
        break
    else:
        print("incorrect input")



