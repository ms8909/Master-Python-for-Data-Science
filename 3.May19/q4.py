def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg
my_list = [1,22,32,12,55,88,76,54,2,1,22,33,44,5,6,6,7,5,0]
print("The average is", cal_average(my_list))