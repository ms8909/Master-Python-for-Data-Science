def convert_to_boolean(string):
  if string.upper() == 'TRUE':
    return True
  elif string.upper() == 'FALSE':
    return False
  else:
    print('Not a boolean!')

def XOR(boolean_1, boolean_2): 
  if isinstance(boolean_1, bool) and isinstance(boolean_2, bool):
    print(boolean_1 != boolean_2)
  else: 
    print('either one or both of the parameters were not boolean!')

boolean_1 = convert_to_boolean(input('Enter True or False = '))
boolean_2 = convert_to_boolean(input('Enter True or False = '))

XOR(boolean_1, boolean_2)





