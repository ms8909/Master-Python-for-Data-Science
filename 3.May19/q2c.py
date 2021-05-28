N= 5
k = 2 * N - 2
# Outer loop in reverse order
for i in range(N, -1, -1):
    # Inner loop will print the number of space.
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    # This inner loop will print the number o stars
    for j in range(1, i +1):
        print(j%2, end=" ")
    print("")
