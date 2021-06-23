def compareTriplets(a, b):
    # Write your code here
    total_a = 0
    total_b = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            total_a = total_a + 1
        elif a[i] < b[i]:
            total_b = total_b + 1
    return (total_a, total_b)