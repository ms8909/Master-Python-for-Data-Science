
def transpose(A):
    for i in range(4):
        for j in range(i, 4):
            
            A[i][j], A[j][i] = A[j][i], A[i][j]
A = [ [27, 28, 41, 94],
    [45, 12, 84, 69],
    [22, 92, 50, 79],
    [51, 72, 68, 97]]
transpose(A)
print("Transposed matrix is")
for i in range(4):
    for j in range(4):
        print(A[i][j], " ", end='')
    print()





