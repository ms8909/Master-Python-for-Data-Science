# Complete the 'migratoryBirds' function below.

def migratoryBirds(arr):
    # Write your code here
    bird_freq = [0, 0, 0, 0, 0, 0]
    for i in range(len(arr)):
        bird_freq[arr[i]] += 1
    return bird_freq.index(max(bird_freq))

