num = int(input('Please enter a positive number = '))
num_list = []

if num < 0:
  print('Negative number is not allowed')

else:
  while num != 1:
    num_list.append(str(num))

    if num % 2 != 0 :
      num = (num * 3) + 1
    else:
      num = int(num / 2)

  num_list.append(str(1))

  print('The collatz chain is: ', '-'.join(num_list))
  print ('Collatz chain length: ', len(num_list))


