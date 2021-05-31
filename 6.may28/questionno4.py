def substitution_cipher(message, offset):
  temp_lst = list(map(lambda x: chr(ord(x) + offset), message))
  return ''.join(temp_lst)

message = input('Please enter your message: ')
offset = int(input('Please enter the offset: '))

print(substitution_cipher(message, offset))