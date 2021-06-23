#!/bin/python3

import math
import os
import random
import re
import sys

def getTotalX(a, b):
    # Write your code here
    maxA = max(a)
    minB = min(b)
    count = 0
    for num in range(maxA, minB + 1):
        left = all([num % numA == 0 for numA in a])
        right = all([numB % num == 0 for numB in b])
        count += left * right
    return count