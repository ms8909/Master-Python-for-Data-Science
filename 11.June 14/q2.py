def staircase(n):
    # Write your code here
    for i in range(1, n + 1):
            print(str('#'*i).rjust(n))