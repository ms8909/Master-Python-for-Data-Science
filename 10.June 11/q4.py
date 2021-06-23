def aVeryBigSum(ar):
    # Write your code here
    sum = 0
    for i in range(len(ar)):
        sum = sum + int(ar[i])
    return sum