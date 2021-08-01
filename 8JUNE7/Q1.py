import math


def fic(num):
    if num > 0:
        product = num * fic(num-1)
        return product
    else:
        return 1


num = 5
fic(num)
