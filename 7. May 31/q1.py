lst = [1,5,67,2,43,6,4,2,2,4,6,2,1,68,5,4 ]

def bubble_sort(list):
  
  temp_bool = False

  while not temp_bool:
    temp_var = None
    count = 1

    for i in range(len(list) - 1):
      if list[i] > list[i + 1]:
        temp_var = list[i]
        list[i] = list[i + 1]
        list[i + 1] = temp_var 
      elif count == (len(list) - 1):
        temp_bool = True
      else:
        count += 1

  print(list)
     


bubble_sort(lst)


