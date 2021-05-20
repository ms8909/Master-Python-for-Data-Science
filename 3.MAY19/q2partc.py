#question no 2 part c
print("  ")
row = 3
m = 2 * row - 2
for i in range(row, -1, -1):
    for j in range(m, 0, -1):
        print(end=" ")
    m = m + 1
    for j in range(0, i + 1):
        print("0", end=" ")
    print("")
