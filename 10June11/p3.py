#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar, ar_count):
    sum = 0
    for i in range(ar_count):
        sum = sum + int(ar[i])
    return sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(str, input().rstrip().split()))

    result = aVeryBigSum(ar, ar_count)

    fptr.write(str(result) + '\n')

    fptr.close()


