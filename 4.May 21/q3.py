import random

num_of_rolls = int(input('Pleas enter the number times you would like to roll the dice? '))
count = 0

for i in range(num_of_rolls):
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  
  dice_sum = dice1 + dice2
  print ('Dice roll {} sum: {}'.format(i + 1, dice_sum))

  if dice_sum == 7:
    count += 1

print('You rolled the lucky number {} times'.format(count))




