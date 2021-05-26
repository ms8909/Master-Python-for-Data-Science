s = input("Please input a string = ").replace(' ', '')
alphabet_lst = list('abcdefghijklmnopqrstuvwxyz')
print(s)

# part 1
def ascii_sum(string):
  sum = 0

  for letter in string:
    sum += ord(letter)

  print('Total ASCII sum: ',sum)

# part 2
def ascii_sum_odd(string):
  sum = 0

  for letter in string:
    if (alphabet_lst.index(letter.lower()) + 1) % 2  != 0:
      sum += ord(letter)
  
  print('ASCII sum of odd-numbered characters: ', sum)

# part 3
def ascii_sum_even(string):
  sum = 0

  for letter in string:
    if (alphabet_lst.index(letter.lower()) + 1) % 2  == 0:
      sum += ord(letter)
  
  print('ASCII sum of even-numbered characters: ', sum)

ascii_sum(s)
ascii_sum_odd(s)
ascii_sum_even(s)