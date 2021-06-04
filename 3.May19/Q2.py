#part a
for i in range(4):
    for j in range (i+1):
        print("*", end="")
    print()

#part b
print(" ")
h = 3
for i in range (h):
    print (" "*(h-i), "*"*(i*2+1))
for i in range (h-2, -1, -1):
    print (" "*(h-i), "*"*(i*2+1))

#part c

print("  ")
rows = 3
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("0", end=" ")
    print("")
