#Linear Search



def LS(lis, num):
    leng = len(lis)
    for i in range(leng):
        if lis[i] == num:
            return i
    return -1


li = [1,2,3,4,5,6]

print(LS(li,3))
        