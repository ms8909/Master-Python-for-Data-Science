def kangaroo(x1, v1, x2, v2):
    # Write your code here
     #max distance kangaroos can go is 10000
    for i in range(10000):
        if x1 + v1 == x2 + v2:
            return 'YES'
        x1 += v1
        x2 += v2
    return 'NO'