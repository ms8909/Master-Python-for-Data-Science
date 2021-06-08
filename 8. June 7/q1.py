lst = [93,1,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ] 

def insertion_sort(list):

  marker = 2
  temp_num = None

  while marker <= len(list):
    
    for j in reversed(range(marker - 1)):
      if list[j] > list[j + 1]:
        temp_num = list[j + 1]
        list[j + 1] = list[j]
        list[j] = temp_num 

    marker += 1

  print(list)



insertion_sort(lst)
