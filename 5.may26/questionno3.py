def dna_transformation(string):
  reversed_str = string[::-1].upper()
  transformed_str = ''

  for letter in reversed_str:
    if letter == 'C':
      transformed_str += 'G'
    elif  letter == 'G':
      transformed_str += 'C'
    elif  letter == 'A':
      transformed_str += 'T'  
    elif  letter == 'T':
      transformed_str += 'A'
  
  print(transformed_str)

def dna_check(string, lst):
  if all(elem in lst for elem in string.upper()) and len(string):
    dna_transformation(string)
  else:
    print('Not a valid dna string')

dna_string = input('Please enter a DNA string = ')
dna_component_lst = ['A','C','G','T']

dna_check(dna_string, dna_component_lst)    
