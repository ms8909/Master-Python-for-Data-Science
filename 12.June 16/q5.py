def birthday(s, d, m):
    # Write your code here
    return sum([1 for i in range(n-m+1) if sum(s[i:i+m])==d]) 