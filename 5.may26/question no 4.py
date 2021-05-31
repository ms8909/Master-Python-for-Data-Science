num = int(input('Please enter a number = '))

def is_prime(number):
  prime_lst = [1]
  for num in range(2, number + 1):
    if num > 1:
      for i in range(2, num):
        if (num % i) == 0:
          break
      else:
        prime_lst.append(num)
  print(prime_lst)



def factors(number):
  factors_lst = []
  for num in range(1, number + 1):
    if number % num == 0:
      factors_lst.append(num)
  print(factors_lst)


def prime_factors(number):
    i = 2
    factors = [1]
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    print(factors)  

prime_factors(num)