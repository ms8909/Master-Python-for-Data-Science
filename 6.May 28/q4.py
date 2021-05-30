list1 = []
s = 'Hi'
offset = 3

for i in s:
    p = list1.append(chr(ord(i) + 3))
    answer = ''.join(list1)

    print(answer)
