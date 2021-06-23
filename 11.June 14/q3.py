def miniMaxSum(arr):
    # Write your code here
    sum = 0
    for i in arr:
        sum += i
        
    min = 10000000000
    max = 0
    for i in arr:
        if max < i:
            max = i
        if min > i:
            min = i
            
    print (sum-max, sum-min)