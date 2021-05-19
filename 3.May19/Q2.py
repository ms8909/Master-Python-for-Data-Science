#Part a
print("  ")
rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end='')
    print('')

#Part b
print("  ")
h = 3
for i in range(h):
    print(" "*(h-i), "*"*(i*2+1))
for i in range(h-2, -1, -1):
    print(" "*(h-i), "*"*(i*2+1))

#Part c
print("  ")
rows = 3
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("1", end=" ")
    print("")

