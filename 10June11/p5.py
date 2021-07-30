#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positiveCounter = 0
    negetiveCounter = 0
    zeroCounter = 0

    for i in range (len(arr)):
        if arr[i] > 0:
            positiveCounter += 1
        elif arr[i] < 0 :
            negetiveCounter +=1
        else:
            zeroCounter += 1

    print("%f"%(positiveCounter / len(arr)))
    print("%f"%(negetiveCounter / len(arr)))
    print("%f"%(zeroCounter / len(arr)))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)