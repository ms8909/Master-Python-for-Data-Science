lst = [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

def selection_sort(list):
  count = 0
  temp_bool = False

  while not temp_bool:
    temp_num = list[count]
    temp_index = 0

    for i in range(count + 1, len(list)):
      if list[i] < temp_num:
        temp_num = list[i]
        temp_index = i

    if count < 14 and temp_index != 0:
      list[temp_index] = list[count]
      list[count] = temp_num
      count += 1
    elif count < 14:
      count += 1
    else:
      temp_bool = True

  print(list)

selection_sort(lst) 